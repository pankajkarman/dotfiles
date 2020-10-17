#################################
    #####    Pankaj    #####
#################################

# my own

alias go='hub browse'
alias ply='sh /home/pankaj/.local/PanoplyJ/panoply.sh'
alias ydlaudio='youtube-dl -x --embed-thumbnail --audio-format mp3'
alias ydl='youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best''
alias blogcon='conda activate blog'
alias con3='export PATH="/home/pankaj/.local/Anaconda3/bin:$PATH"'
alias con2='export PATH="/home/pankaj/.local/Anaconda2/bin:$PATH"'
alias proxyon='export all_proxy=http://172.16.2.30:8080'
alias proxyoff='export all_proxy='
alias remote='jupyter notebook --no-browser --port=8889'
alias remote2='con2; jupyter notebook --no-browser --port=8889'
alias remote3='con3; jupyter notebook --no-browser --port=8889'
alias serve='ssh -N -f -L localhost:8888:localhost:8889'
alias pyget='conda install -c conda-forge'
alias repo='sudo mknod -m 666 /dev/fuse c 10 229; sshfs jayan@10.57.12.190:/home/jayan/repo ~/Desktop/repo'
alias urepo='fusermount -u ~/Desktop/repo'
alias cputemp='sensors | grep Core'
alias wakelab='/usr/bin/wakeonlan 00:11:32:11:15:FC'
alias rcon='conda activate rstudio'
alias deploy='nikola github_deploy'
alias launch='nikola auto'
alias netrestart='sudo systemctl restart network-manager'

alias c='clear'
alias matlab='sudo /home/pankaj/.local/MATLAB/R2016a/bin/matlab -nosplash'
alias book2='con2; jupyter notebook'
alias book3='con3; jupyter notebook'
alias jlab='jupyter-lab'

# reset bashrc
alias ssh='ssh -X'
alias src='source ~/.bashrc'
alias rc='vi ~/.bashrc'
alias al='vi ~/.bash_aliases'
alias lssh='cat ~/.ssh/config'

# Alias quotidiens
alias ssudo='sudo -sE'
alias ss='ssudo'
alias sudo='sudo -E'
alias get="sudo apt-get install -y"
alias remove="sudo apt-get remove"

# Alias some common chmod amounts
alias mx='chmod a+x'
alias 000='chmod -R 000'
alias 644='chmod -R 644'
alias 666='chmod -R 666'
alias 755='chmod -R 755'
alias 777='chmod -R 777'

# ls
alias ls='ls --color=auto'
alias lh='ls -a|grep "^\."' #  hidden only 
#alias ll='ls -lAh'
alias lx='ls -lXB'          #  Sort by extension.
alias lk='ls -lSrh'         #  Sort by size, biggest last.
alias lt='ls -ltr'          #  Sort by date, most recent last.
alias lc='ls -ltcr'         #  Sort by/show change time,most recent last.
alias lu='ls -ltur'         #  Sort by/show access time,most recent last.

alias ll="ls -lv --group-directories-first"
alias lm='ll |more'         #  Pipe through 'more'
alias lr='ll -R'            #  Recursive ls.
alias la='ll -A'            #  Show hidden files.
alias tree='tree -Csuh'     #  Nice alternative to 'recursive ls' ...

#  grep
alias grep='grep --color=auto'
alias pg='ps aux | grep'

#logs
alias weblogtail="tail -F /var/log/apache2/*"        # watch web server log
alias logs="tail -F /var/log/*.log /var/log/*/*.log /var/log/syslog"  # watch various current logs
alias mem='egrep "Mem|Cache|Swap" /proc/meminfo'

## pass options to free ##
alias meminfo='free -m -l -t'
 
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
 
## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
 
## Get server cpu info ##
alias cpuinfo='lscpu'
 
## older system use /proc/cpuinfo ##
##alias cpuinfo='less /proc/cpuinfo' ##
 
## get GPU ram on desktop / laptop##
alias gpumeminfo='grep -i --color memory /var/log/Xorg.0.log'


# reboot / halt / poweroff
alias reboot='sudo /sbin/reboot'
alias poweroff='sudo /sbin/poweroff'
alias halt='sudo /sbin/halt'
alias shutdown='sudo /sbin/shutdown'

# navigation
alias cd..='cd ..'
alias ..='cd ..'
alias ...='cd ../../'
alias ....='cd ../../..'

#command history
alias h='history'
alias path='echo -e ${PATH//:/\\n}'
alias j='jobs -l'

# Alias de sécurité
alias rm='rm --preserve-root'

alias duh="du -h "                       # use human-readable sizes
alias dud="du --max-depth=1 -h "         # human, one-deep (often more readable)
alias lslast="ls -lrt "                  # show last modified last
alias lsd='find * -prune -type d -ls'    # 'list directories under curdir'
alias hexdump='od -t x1z'                # "show hex representation, of single bytes at a time, show text alongside"
alias lesscol="less -R"                  # less that allows color (...control codes)

# change default verbosity
alias df="df -hT "                       # use human-readable sizes and show filesystem type
alias bzip2="bzip2 -p "                  # always print progress when bzipping
alias pstree='pstree -pu '               # always show pid, and show usernames where UID changes
alias psme='ps -fHu $USER'

# change default behaviour:
alias bc="bc -lq "                       # bc always does float calculations

# Récupérer son IP externe
alias myip='wget -qO- http://icanhazip.com'

# Afficher l'heure actuelle
alias now='date +"%T"'

# Sortie de mount plus lisible
alias mount='mount | column -t'

# Affiche le ports ouverts
alias ports='netstat -tulanp'

# Show which applications are connecting to the network.
alias listen="lsof -P -i -n" 

# Mise à jour toute en un
alias update='sudo apt update && sudo apt dist-upgrade'
alias safe-update='sudo apt update && sudo apt upgrade'

# Toujours permettre de continuer un téléchargement wget interrompu
alias wget='wget -c'
alias dlpage="wget -r -l 1 "             # save page and direct links


# Copie le contenu d'un fichier dans le presse-papier
alias copy='xsel -i --clipboard <'

# IPython Notebook
alias book='jupyter notebook'

# Met à jour tous les paquets pip
alias pipupgrade="pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U"
