---
title: "Build the fancy iTerm2"
date: 2022-07-21
author: pengjianqing
categories: ['Tech']
---

## Install iTerm2

Before to build the fancy Terminal, it need to install the iTerm first.

- https://iterm2.com/index.html

The config file will be ~/.zshrc, so for the themes and plugins, need to update this config file accordingly.

## Install oh my zsh

- https://github.com/ohmyzsh/ohmyzsh

```
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
```

## Install Plugins

- [https://github.com/marlonrichert/zsh-autocomplete](https://github.com/marlonrichert/zsh-autocomplete)
- https://github.com/zsh-users/zsh-autosuggestions

## Install autojump

- https://github.com/wting/autojump

```
`brew install autojump`
```

## Install zsh-syntax-highlight

- [https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)

```
`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
plugins=( [plugins...] zsh-syntax-highlighting)`
```

## Themes

- [https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes](https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes)

I choose this some

- https://github.com/ChesterYue/ohmyzsh-theme-passion

## Install thefuck

```
**brew install thefuck**# After installation, add these two lines to your ***.zshrc*** file
eval "$(thefuck --alias)"
alias fuck='fuck -y'
```

## Fonts

Install the Fonts

- https://github.com/powerline/fonts

```
`# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts`
```

## .zshrc config file

```
`export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="random"
ZSH_THEME="wedisagree"
ZSH_THEME="apple"
ZSH_THEME="simple"
ZSH_THEME="eastwood"
ZSH_THEME="agnoster"
ZSH_THEME="passion"
plugins=(git)
source $ZSH/oh-my-zsh.sh
plugins=(git textmate ruby autojump osx mvn gradle adb common-aliases jira vagrant zsh-autosuggestions zsh-syntax-highlighting)
alias vim="nvim"
alias cls='clear'
alias ll='ls -l'
alias la='ls -a'
alias vi='vim'
alias javac="javac -J-Dfile.encoding=utf8"
alias grep="grep --color=auto"
alias -s html=nvim
alias -s rb=nvim
alias -s py=nvim
alias -s js=nvim
alias -s c=nvim
alias -s java=nvim
alias -s txt=nvim
alias -s xml=nvim
alias -s gradle=nvim
alias -s md=nvim
alias -s gz='tar -xzvf'
alias -s tgz='tar -xzvf'
alias -s zip='unzip'
alias -s bz2='tar -xjvf'
[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh
export PATH="${PATH}:${HOME}/Library/Android/sdk/emulator/"
export PATH="${PATH}:${HOME}/Library/Android/sdk/platform-tools"
export PATH="${PATH}:${HOME}/Library/Android/sdk/tools"
export PATH="${PATH}:${HOME}/Library/Android/sdk/tools/bin/"
export PATH="${PATH}:/Library/Android/sdk/build-tools/31.0.0-rc3/"
export PATH="${PATH}:/usr/local/opt/gnu-sed/bin"
export PATH="${PATH}:/usr/local/bin"
export ANDROID_HOME="${HOME}/Library/Android/sdk"
export ANDROID_SDK_ROOT=${ANDROID_HOME}
zstyle ':completion:*:*:git:*' script ~/.git-completion.zsh
export CUDA_HOME=/usr/local/cuda
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
alias sf_adbforward="adb forward tcp:8080 tcp:8080 && adb forward tcp:14023 tcp:14023"
alias ginstall="cd ${HOME}/workspace/androidrepo && ./gradlew installB_cnDebug && sf_startapp"
echo "set jdk11" && jdk11
alias adb_rpi3_home_eth0="adb connect 192.168.31.135"
alias adb_rpi3_home_wlan0="adb connect 192.168.31.180"
alias rm="/usr/local/bin/rmtrash.sh"
alias markdown_convert="gsed -i -e '/alt text/s/^/\`\`\`/g' -e  '/alt text/s/$/\`\`\`/g'"
alias markdown_revert="gsed -i '/alt text/s/\`\`\`//g'"
export PATH=${PATH}:/usr/local/go/bin
alias json="python -m json.tool"
set -o vi
source ~/.yoda/yoda.sh
alias lsusb="system_profiler SPUSBDataType"
alias nmapw="nmap -p- -A -v -T4 "
alias rm="trash"
eval "$(thefuck --alias)"
alias fuck='fuck -y'
[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
export PATH="$PATH:$HOME/.rvm/bin"
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles
#source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.oh-my-zsh/custom/plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh`
```