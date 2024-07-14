Readme⽂件，⽤来说明运⾏源代码所需要执⾏的命令，环境依赖等；
1.源代码需要执行的命令
        见贪吃蛇研究这个md，里面把函数和存在意义讲的很清楚了
        
2.环境依赖：
        linux系统
        通过env命令得知：
        SHELL=/bin/bash
        COLORTERM=truecolor
        WSL2_GUI_APPS_ENABLED=1
        TERM_PROGRAM_VERSION=1.76.1
        CONDA_EXE=/home/rainy/miniconda3/bin/conda
        _CE_M=
        WSL_DISTRO_NAME=Ubuntu-20.04
        NAME=LAPTOP-V6AEDB8B
        PWD=/home/rainy/python
        LOGNAME=rainy
        CONDA_PREFIX=/home/rainy/miniconda3
        VSCODE_GIT_ASKPASS_NODE=/home/rainy/.vscode-server/bin/5e805b79fcb6ba4c2d23712967df89a089da575b/node
        HOME=/home/rainy
        LANG=C.UTF-8
        WSL_INTEROP=/run/WSL/1132_interop
        LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
        WAYLAND_DISPLAY=wayland-0
        CONDA_PROMPT_MODIFIER=(base) 
        GIT_ASKPASS=/home/rainy/.vscode-server/bin/5e805b79fcb6ba4c2d23712967df89a089da575b/extensions/git/dist/askpass.sh
        VSCODE_GIT_ASKPASS_EXTRA_ARGS=
        LESSCLOSE=/usr/bin/lesspipe %s %s
        TERM=xterm-256color
        _CE_CONDA=
        LESSOPEN=| /usr/bin/lesspipe %s
        USER=rainy
        VSCODE_GIT_IPC_HANDLE=/mnt/wslg/runtime-dir/vscode-git-68e79de418.sock
        CONDA_SHLVL=1
        DISPLAY=:0
        SHLVL=1
        CONDA_PYTHON_EXE=/home/rainy/miniconda3/bin/python
        XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir
        CONDA_DEFAULT_ENV=base
        WSLENV=VSCODE_WSL_EXT_LOCATION/up
        VSCODE_GIT_ASKPASS_MAIN=/home/rainy/.vscode-server/bin/5e805b79fcb6ba4c2d23712967df89a089da575b/extensions/git/dist/askpass-main.js
        XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
        PATH=/home/rainy/.vscode-server/bin/5e805b79fcb6ba4c2d23712967df89a089da575b/bin/remote-cli:/home/rainy/.local/bin:/home/rainy/miniconda3/bin:/home/rainy/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0:/mnt/c/Windows/System32/OpenSSH:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Users/Rainy/Mingw64.zip/mingw64/mingw64/bin:/mnt/c/Users/Git/cmd:/mnt/c/Program Files/dotnet:/mnt/c/Users/Rainy/AppData/Local/Programs/Python/Python310/Scripts:/mnt/c/Users/Rainy/AppData/Local/Programs/Python/Python310:/mnt/c/Users/Rainy/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/Rainy/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/c/c++/mingw64/bin:/snap/bin
        HOSTTYPE=x86_64
        PULSE_SERVER=unix:/mnt/wslg/PulseServer
        TERM_PROGRAM=vscode
        VSCODE_IPC_HOOK_CLI=/mnt/wslg/runtime-dir/vscode-ipc-9443407f-6304-4993-984e-23ee4af4fb96.sock
        _=/usr/bin/env

        以下是本人的安装包一览：
        # packages in environment at /home/rainy/miniconda3:
        #
        # Name                    Version                   Build  Channel
        _libgcc_mutex             0.1                        main    defaults
        _openmp_mutex             5.1                       1_gnu    defaults
        brotlipy                  0.7.0           py39h27cfd23_1003    defaults
        ca-certificates           2022.10.11           h06a4308_0    defaults
        certifi                   2022.12.7        py39h06a4308_0    defaults
        cffi                      1.15.1           py39h5eee18b_3    defaults
        charset-normalizer        2.0.4              pyhd3eb1b0_0    defaults
        conda                     22.11.1          py39h06a4308_4    defaults
        conda-content-trust       0.1.3            py39h06a4308_0    defaults
        conda-package-handling    1.9.0            py39h5eee18b_1    defaults
        cryptography              38.0.1           py39h9ce1e76_0    defaults
        idna                      3.4              py39h06a4308_0    defaults
        ld_impl_linux-64          2.38                 h1181459_1    defaults
        libffi                    3.4.2                h6a678d5_6    defaults
        libgcc-ng                 11.2.0               h1234567_1    defaults
        libgomp                   11.2.0               h1234567_1    defaults
        libstdcxx-ng              11.2.0               h1234567_1    defaults
        ncurses                   6.3                  h5eee18b_3    defaults
        openssl                   1.1.1s               h7f8727e_0    defaults
        pip                       22.3.1           py39h06a4308_0    defaults
        pluggy                    1.0.0            py39h06a4308_1    defaults
        pycosat                   0.6.4            py39h5eee18b_0    defaults
        pycparser                 2.21               pyhd3eb1b0_0    defaults
        pyopenssl                 22.0.0             pyhd3eb1b0_0    defaults
        pysocks                   1.7.1            py39h06a4308_0    defaults
        python                    3.9.15               h7a1cb2a_2    defaults
        readline                  8.2                  h5eee18b_0    defaults
        requests                  2.28.1           py39h06a4308_0    defaults
        ruamel.yaml               0.17.21          py39h5eee18b_0    defaults
        ruamel.yaml.clib          0.2.6            py39h5eee18b_1    defaults
        setuptools                65.5.0           py39h06a4308_0    defaults
        six                       1.16.0             pyhd3eb1b0_1    defaults
        sqlite                    3.40.0               h5082296_0    defaults
        tk                        8.6.12               h1ccaba5_0    defaults
        toolz                     0.12.0           py39h06a4308_0    defaults
        tqdm                      4.64.1           py39h06a4308_0    defaults
        tzdata                    2022g                h04d1e81_0    defaults
        urllib3                   1.26.13          py39h06a4308_0    defaults
        wheel                     0.37.1             pyhd3eb1b0_0    defaults
        xz                        5.2.8                h5eee18b_0    defaults
        zlib                      1.2.13               h5eee18b_0    defaults