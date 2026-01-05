---
title: "Android:Google 翻译前端"
date: 2009-06-04
author: pengjianqing
categories: ['Android']
tags: ['Android', 'Database，Google', 'File', 'Spinner', 'Translator']
---

Update
做了一个Google 翻译前端。
涉及到Android  Spinner用法，网络数据解析，数据库操作，以及文件的读写（包含读写中文（UTF））

源码可以在这里下载到。
http://github.com/pjq/GTranslator/tree/master
如果觉得这个程序有用，也请顶一下了，谢谢 。

可以选择要翻译的语言。

主界面：
[![](http://lh3.ggpht.com/_GxH7-x2-l3Y/SifiR9dwBCI/AAAAAAAAAOA/wQ0ekzlhM7A/s800/2009-06-04-225725_384x733_scrot.jpg)](http://picasaweb.google.com/lh/photo/vqfUo9zzqumAzfs22NtdPQ?feat=embedwebsite)发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

查询历史，用到的是数据库：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/SifiXyltkvI/AAAAAAAAAOE/ZykrT5roXv8/s800/2009-06-04-225748_377x729_scrot.jpg)](http://picasaweb.google.com/lh/photo/78W9b8Vja7HS6LJCXnMIrg?feat=embedwebsite)发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

这里也是查询历史用的是文件读写：
[![](http://lh3.ggpht.com/_GxH7-x2-l3Y/Sifibw0o0TI/AAAAAAAAAOI/5cfVbHOG1AY/s800/2009-06-04-225813_379x731_scrot.jpg)](http://picasaweb.google.com/lh/photo/UD99VCTYh3RZcWi9E8rw6A?feat=embedwebsite)发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

翻译语言选择：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/Sififul7ByI/AAAAAAAAAOM/72ErFDIlBD4/s800/2009-06-04-225831_376x731_scrot.jpg)](http://picasaweb.google.com/lh/photo/842sQQDwCv7Hc3RImz4hhA?feat=embedwebsite)发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

主要Android 源码：

GTranslator.java
```

package com.percy.gtranslator;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.impl.cookie.DateParseException;

import android.R.integer;
import android.app.Activity;
import android.database.Cursor;
import android.database.DatabaseUtils;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.view.ViewManager;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Spinner;

public class GTranslator extends Activity implements OnClickListener
{
	/** Called when the activity is first created. */
	private static final boolean	bAtOffice		= false;

	private TextView				textViewTranslate;
	private Button					buttonTranslate;
	private EditText				editTextTranslate;

	private TextView				promptTextView;
	private Spinner					usedTranslatorSpinner;
	private Spinner					fromSpinner;
	private Spinner					toSpinner;
	private Button					translateButton;
	private Button					clearButton;
	private Button					readDatabaseButton;
	private Button					readFileButton;
	private TextView				translatedTextView;
	private EditText				toTranslateEditText;

	private DBAdapter				dbAdapter;

	private static final String[]	mCountries		=
													{ "en", "zh-CN", "it",
			"zh_TW", "ja", "de", "el", "ko", "ko", "ru", "th", "fr", "fr" };

	private static final String[]	translateWeb	=
													{ "google", "yahoo",
			"baidu"								};
	private List			allcountries;

	private ArrayAdapter	fromSpinnerAdapter;

	private ArrayAdapter	translateWebAdapter;
	private List			allTranslateWeb;

	private String					fromString;
	private String					toString;

	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		setTheme(android.R.style.Theme_NoTitleBar);

		this.dbAdapter = new DBAdapter(this);
		this.dbAdapter.open();

		promptTextView = (TextView) findViewById(R.id.promptTextView);
		usedTranslatorSpinner = (Spinner) findViewById(R.id.usedTranslatorSpinner);
		fromSpinner = (Spinner) findViewById(R.id.fromSpinner);
		toSpinner = (Spinner) findViewById(R.id.toSpinner);
		translateButton = (Button) findViewById(R.id.translateButton);
		clearButton = (Button) findViewById(R.id.clearButton);
		readDatabaseButton = (Button) findViewById(R.id.readDatabaseButton);
		readFileButton = (Button) findViewById(R.id.readFileButton);
		translatedTextView = (TextView) findViewById(R.id.translatedTextView);
		toTranslateEditText = (EditText) findViewById(R.id.toTranslateEditText);

		toTranslateEditText.setCursorVisible(true);
		toTranslateEditText.setVerticalScrollBarEnabled(true);

		translateButton.setOnClickListener(this);
		clearButton.setOnClickListener(this);
		readDatabaseButton.setOnClickListener(this);
		readFileButton.setOnClickListener(this);

		allcountries = new ArrayList();

		for (int i = 0; i < mCountries.length; i++)
		{
			allcountries.add(mCountries[i]);
		}

		fromSpinnerAdapter = new ArrayAdapter(this,
				android.R.layout.simple_spinner_item, allcountries);// simple_spinner_item
		fromSpinnerAdapter
				.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);// simple_spinner_dropdown_item
		fromSpinner.setAdapter(fromSpinnerAdapter);
		fromSpinner.setSelection(0);
		toSpinner.setAdapter(fromSpinnerAdapter);
		toSpinner.setSelection(1);

		allTranslateWeb = new ArrayList();
		for (int i = 0; i < translateWeb.length; i++)
		{
			allTranslateWeb.add(translateWeb[i]);
		}

		translateWebAdapter = new ArrayAdapter(this,
				android.R.layout.simple_spinner_item, allTranslateWeb);
		translateWebAdapter
				.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
		usedTranslatorSpinner.setAdapter(translateWebAdapter);

		listItemFromDatabase();
	}

	@Override
	public void onClick(View v)
	{
		int id = v.getId();
		if (id == R.id.translateButton)
		{
			translatedTextView.setText("Connecting...");
			String toTranslateTextString = toTranslateEditText.getText()
					.toString();
			String tempString = toTranslateTextString.replace(" ", "%20");
			fromString = mCountries[fromSpinner.getSelectedItemPosition()];
			toString = mCountries[toSpinner.getSelectedItemPosition()];
			String queryString = tempString + "&langpair=" + fromString + "%7C"
					+ toString;
			// String queryString = tempString + "&langpair=en%7Czh-CN";
			// textViewTranslate.setText("queryString:"+toTranslateTextString+":"+'\n');

			String rawData = getRawData(queryString);
			if (null != rawData)
			{
				String parsedDataString = getData(rawData);
				if (null == parsedDataString||""==parsedDataString)
				{
					translatedTextView.setText("Not found");
				} else
				{
					translatedTextView.setText(parsedDataString);
					dbAdapter.insertItem(toTranslateTextString, parsedDataString);

					FileAccess.writeFile(this, toTranslateTextString + ":"
							+ parsedDataString);
				}

			} else
			{
				translatedTextView.setText("Translate failed!");
			}
		} else if (id == R.id.clearButton)
		{
			toTranslateEditText.setText("");
			translatedTextView.setText("");
		} else if (id == R.id.readDatabaseButton)
		{
			translatedTextView.setText("Search history(Read Database):" + '\n');
			Cursor mCursor = this.dbAdapter.getAllItem();
			if (mCursor.moveToFirst())
			{
				do
				{
					int index = mCursor.getColumnIndex(DBAdapter.TOTRANSLATETEXT);
					String fromTextString = mCursor.getString(index);
					index = mCursor.getColumnIndex(DBAdapter.TRANSLATEDTEXT);
					String toTextString = mCursor.getString(index);
					translatedTextView
							.append("**********************************" + '\n');
					translatedTextView.append(fromTextString + ":" + toTextString
							+ '\n');

				} while (mCursor.moveToNext());
				translatedTextView
						.append("**********************************" + '\n');
			}

		} else if (id == R.id.readFileButton)
		{

			translatedTextView
					.setText("Search history(Read File):" + '\n');
			String readTextString = FileAccess.readFile(this, "test.txt");
			translatedTextView.append("" + readTextString);

		}
	}

	@Override
	protected void onDestroy()
	{
		// TODO Auto-generated method stub

		super.onDestroy();
		dbAdapter.close();
	}

	public static String getData(String dataString)
	{
		int index1 = dataString.indexOf(",");
		String string1 = dataString.substring(1, index1);
		String string2 = string1.replace("\"", "");

		int index2 = string2.lastIndexOf(":");
		String string3 = string2.substring(index2);
		String string4 = string3.replace("}", "");
		String string5 = string4.replace(":", "");
		return string5;
	}

	public static String getRawData(String string)
	{

		String dataString = null;
		// String queryString = "hello%20world&langpair=en%7Czh-CN";
		String queryString = string;
		try
		{
			URL url;
			if (bAtOffice)
			{
				url = new URL("http://10.85.40.153:8000/a.xml");
			} else
			{
				url = new URL(
						"http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q="
								+ queryString);
			}

			URLConnection conn = url.openConnection();
			conn.connect();
			BufferedReader reader = new BufferedReader(new InputStreamReader(
					conn.getInputStream()));

			byte buffer[] = new byte[1024];

			// bis.r
			String readerString;
			while ((readerString = reader.readLine()) != null)
			{
				dataString += readerString;
			}

			reader.close();
			// is.close();

		} catch (IOException e)
		{
			System.out.print("Net work error");
		}
		return dataString;

	}

	public void createTable(String tableName, String[] columnNames)
			throws DateParseException
	{
		StringBuffer sql = new StringBuffer("Create table if not exists");
		sql.append(tableName);
		sql.append("(");
		int length = columnNames.length - 1;
		for (int i = 0; i <= length; i++)
		{
			sql.append(columnNames[i]);
			sql.append("varchar");
		}
		sql.append(");");

	}

	public void listItemFromDatabase()
	{

		translatedTextView.append("Search history:" + '\n');
		Cursor mCursor = this.dbAdapter.getAllItem();
		if (mCursor.moveToFirst())
		{
			do
			{
				int index = mCursor.getColumnIndex(DBAdapter.TOTRANSLATETEXT);
				String fromTextString = mCursor.getString(index);
				index = mCursor.getColumnIndex(DBAdapter.TRANSLATEDTEXT);
				String toTextString = mCursor.getString(index);
				translatedTextView
						.append("**********************************" + '\n');
				translatedTextView.append(fromTextString + ":" + toTextString
						+ '\n');

			} while (mCursor.moveToNext());
			translatedTextView
					.append("**********************************" + '\n');
		}

		translatedTextView
				.append("#################Read File###################" + '\n');
		String readTextString = FileAccess.readFile(this, "test.txt");
		translatedTextView.append("" + readTextString);

	}

}

```

DBAdapter.java

```

package com.percy.gtranslator;

import android.content.ContentValues;

import android.content.Context;

import android.database.Cursor;

import android.database.SQLException;

import android.database.sqlite.SQLiteDatabase;

import android.database.sqlite.SQLiteOpenHelper;

import android.database.sqlite.SQLiteDatabase.CursorFactory;

import android.text.StaticLayout;

public class DBAdapter

{

	public final static String	KEYID			= "_id";

	public final static String	TOTRANSLATETEXT	= "ToTranslateText";

	public final static String	TRANSLATEDTEXT	= "TranslatedText";

	public final static String	TABLENAME		= "TRANSLATOR";

	public final static String	DATABASENAME	= "TRANSLATORDATABASE";

	public final static int		DATABASEVERSION	= 1;

	private static final String	CREATETABLE		= "create table "

														+ TABLENAME

														+ " ("

														+ KEYID

														+ " integer primary key autoincrement,"

														+ TOTRANSLATETEXT

														+ " text not null, "

														+ TRANSLATEDTEXT

														+ " text not null);";

    private static final String DATABASE_CREATE =

        "create table titles (_id integer primary key autoincrement, "

        + "isbn text not null, title text not null, "

        + "publisher text not null);";

	private DatabaseHelper		DBHelper;

	private SQLiteDatabase		db;

	private Context				context;

	public DBAdapter(Context context)

	{

		this.context = context;

		this.DBHelper = new DatabaseHelper(context);

	}

	public static class DatabaseHelper extends SQLiteOpenHelper

	{

		// public DatabaseHelper(Context context, String name, CursorFactory

		// factory, int version)

		public DatabaseHelper(Context context)

		{

			super(context, DATABASENAME, null, DATABASEVERSION);

			// TODO Auto-generated constructor stub

		}

		@Override

		public void onCreate(SQLiteDatabase db)

		{

			// TODO Auto-generated method stub

			db.execSQL(CREATETABLE);

		}

		@Override

		public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion)

		{

			// TODO Auto-generated method stub

		}

	}

	public void open() throws SQLException

	{

		db = this.DBHelper.getWritableDatabase();

		// return this;

	}

	public void close()

	{

		DBHelper.close();

	}

	public long insertItem(String fromText, String toText)

	{

		ContentValues contentValues = new ContentValues();

		contentValues.put(TOTRANSLATETEXT, fromText);

		contentValues.put(TRANSLATEDTEXT, toText);

		return db.insert(TABLENAME, null, contentValues);

	}

	public Cursor getItem(long id) throws SQLException

	{

		// db.query(TABLENAME, new String[]{}, selection, selectionArgs,

		// groupBy, having, orderBy);

		Cursor mCursor = db.query(TABLENAME, new String[]

		{ TOTRANSLATETEXT, TRANSLATEDTEXT }, KEYID + "=" + id, null, null,

				null, null);

		if (mCursor != null)

		{

			mCursor.moveToFirst();

		}

		return mCursor;

	}

	public Cursor getAllItem() throws SQLException

	{

		Cursor mCursor = db.query(TABLENAME, new String[]

		{ TOTRANSLATETEXT, TRANSLATEDTEXT }, null, null, null, null, null);

		return mCursor;

	}

}

```

FileAccess.java
```

package com.percy.gtranslator;

import java.io.BufferedInputStream;

import java.io.BufferedReader;

import java.io.DataInputStream;

import java.io.DataOutputStream;

import java.io.File;

import java.io.FileInputStream;

import java.io.FileNotFoundException;

import java.io.FileOutputStream;

import java.io.IOException;

import java.io.InputStream;

import java.io.InputStreamReader;

import java.io.OutputStreamWriter;

import java.nio.CharBuffer;

import android.R.integer;

import android.content.Context;

import android.content.res.Resources;

import android.widget.Toast;

public class FileAccess

{

	public static String	fileName	= "";

	public static String readFile(Context context, String file)

	{

		fileName = file;

		String data = "";

		FileInputStream fi = null;

		DataInputStream dis = null;

		InputStreamReader isr = null;

		// if don't exist,just create the file.

		FileOutputStream fos;

		try

		{

			// fos = context.openFileOutput(fileName,

			// context.MODE_WORLD_WRITEABLE);

			// fos.flush();

			// fos.close();

			fi = context.openFileInput(fileName);

			isr = new InputStreamReader(fi);

			dis = new DataInputStream(fi);

			char[] buffer = new char[1024];

			String line;

			while ((line = dis.readUTF()) != null)

			{

				data += line;

			}

			isr.close();

			dis.close();

			fi.close();

		} catch (Exception e)

		{

			// TODO: handle exception

		}

		return data;

	}

	public static void writeFile(Context context, String toWriteString)

	{

		try

		{

			FileOutputStream fos = context.openFileOutput(fileName,

					context.MODE_APPEND);

			//OutputStreamWriter dos = new OutputStreamWriter(fos);

			// dos.writeChars(toWriteString);

			DataOutputStream dos = new DataOutputStream(fos);

			dos.writeUTF(toWriteString+'\n');

			dos.flush();

			fos.flush();

			dos.close();

			fos.close();

		} catch (FileNotFoundException e)

		{

			// TODO Auto-generated catch block

			Toast.makeText(context, "File not found", 4000).show();

			e.printStackTrace();

		} catch (IOException e)

		{

			// TODO Auto-generated catch block

			e.printStackTrace();

		}

	}

}

```