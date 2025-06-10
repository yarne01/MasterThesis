#! /usr/bin/bash


#consts / settings
FormatDate="%Y_%m_%d__%H_%M_%S"

OUTPUT_DIR="OUTPUT"                     ; mkdir -p "$OUTPUT_DIR"
    O_COMPILED="$OUTPUT_DIR/COMPILED"   ; mkdir -p "$O_COMPILED"
    O_LATEX="$OUTPUT_DIR/LATEX"         ; mkdir -p "$O_LATEX"
    O_LOGS="$OUTPUT_DIR/LOGS"           ; mkdir -p "$O_LOGS"
LATEX="LATEX"                           # ; mkdir -p "$LATEX"
max_width=90





# Begin Calcs
t0=$(date +$FormatDate);
log_file=$OUTPUT_DIR/LOG.log
SECONDS=0

function echo(){ builtin echo "$@" | tee -a $log_file;}
function Echo { while IFS= read -r lijn || [ -n "$lijn" ]; do echo "$lijn"; done }


# : voor error wanneer geen ander input
enable_python=false
enable_c=false
enable_rust=false
enable_fortran=false
enable_latex=false
while getopts ":a:bF:pcrfl" opt; do
  case $opt in
    p) enable_python=true;;
    c) enable_c=true;;
    r) enable_rust=true;;
    f) enable_fortran=true;;
    l) enable_latex=true;;
    a)
      arg_a="$OPTARG"
      echo "Option -a with argument: $arg_a"
      ;;
    b)
      flag_b=true
      echo "Option -b is present"
      ;;
    F)
      output_file="$OPTARG"
      echo "Option -f with argument: $output_file"
      ;;
    \?)
      echo "Invalid option: -$OPTARG"
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument."
      exit 1
      ;;
  esac
done





# example(){
# echo The function location is $0
        # echo There are $# arguments
        # echo "Argument 1 is $1"
        # echo "Argument 2 is $2"
        # echo "<$@>" and "<$*>" are the same.
        # echo List the elements in a for loop to see the difference!
        # echo "* gives:"
        # for arg in "$*"; do echo "<$arg>"; done
        # echo "@ gives:"
        # for arg in "$@"; do echo "<$arg>"; done
        
        # return 100
   # }
# example_output=$(example 1 2 3)


# https://askubuntu.com/questions/528928/how-to-do-underline-bold-italic-strikethrough-color-background-and-size-i
function print_midden {
    text="";    if (($# > 0)); then text=$1; fi
    
    #consts / settings
    symbol="-"
    text="[ $text ]"
    
    # Centering of text
    begin=$((($max_width-${#text})/2))
    textBuffer=""
    for ((i=0; i<$begin; i++)); do textBuffer+="$symbol"; done
    textBuffer+=$text
    for ((i=${#textBuffer}; i<$max_width; i++)); do textBuffer+="$symbol"; done
    
    echo "$textBuffer"
}

function print_hfill {
    text_begin="";    if (($# > 0)); then text_begin=$1; fi
    text_einde="";    if (($# > 1)); then text_einde=$2; fi

    #consts / settings
    symbol=" "
    
    # Centering of text
    begin=$(($max_width-(${#text_begin} + ${#text_einde})))
    textBuffer=$text_begin
    for ((i=0; i<$begin; i++)); do textBuffer+="$symbol"; done
    textBuffer+=$text_einde
    # for ((i=${#textBuffer}; i<$max_width; i++)); do textBuffer+="$symbol"; done
    
    echo "$textBuffer"
}

function print_einde { print_hfill "" $1;}

function plaats {
    # args
    text="";    if (($# > 0)); then text=$1; fi
    lijnen=5;   if (($# > 1)); then lijnen=$2; fi
    
    # Lege lijnen
    for ((i=0; i<$lijnen; i++)); do echo; done
    
    print_midden "$text"
}

function do_c {
    filename="";    if (($# > 0)); then filename=$1; fi
    
    # plaats "$filename"
    
    compile_output=$(mktemp)
    # Fuck sake met geen output 
    if g++ -g -o $O_COMPILED/$filename.out $filename -Wall $flags_c 2> "$compile_output"; then compiled=true; else compiled=false; fi
    
    print_hfill "$filename" "Compile"
    
    Echo < "$compile_output"
    
    # while IFS= read -r line || [ -n "$line" ]; do
        # echo "$line"
    # done < "$compile_output"
    rm "$compile_output"
    
    if $compiled; then
        print_hfill "$filename" "Run"
        # Per chatGPT so both real-time AND line-break
        ./$O_COMPILED/$filename.out | Echo
    fi
    
}

function do_fortran {
    filename="";    if (($# > 0)); then filename=$1; fi
    
    # plaats "$filename"
    
    compile_output=$(mktemp)
    # Fuck sake met geen output 
    
    if gfortran $filename -o $O_COMPILED/$filename.out $flags_f 2> "$compile_output"; then compiled=true; else compiled=false; fi
    
    
    print_hfill "$filename" "Compile"
    Echo < "$compile_output"
    # while IFS= read -r line || [ -n "$line" ]; do
        # echo "$line"
    # done < "$compile_output"
    rm "$compile_output"
    
    if $compiled; then
        print_hfill "$filename" "Run"
        # Per chatGPT so both real-time AND line-break
        ./$O_COMPILED/$filename.out | Echo
    fi
}


flags_c="-lsfml-graphics -lsfml-window -lsfml-system -fopenmp"
flags_f="-fopenmp"
flags_l="-output-directory=$O_LATEX -output-format=pdf -interaction=nonstopmode"


rm $log_file
clear
echo Created At \"$t0\"

plaats "Listing all Files"    
    ls -alhF --color=auto | Echo

if $enable_c        ; then plaats "C part right here"
    do_c "test.cpp"
    for ((i=0; i<5; i++)); do echo; done
    do_c "Meeting1.cpp"
fi

if $enable_fortran  ; then plaats "Fortran part right here"
    do_fortran "test.f90"
fi

if $enable_python   ; then plaats "Executing Python"
        print_einde "test.py"
        
        python3 test.py | Echo
fi

if $enable_rust     ; then plaats "Executing Rust"
        cargo run | Echo
fi


if $enable_latex    ; then plaats "Compiling LaTeX"
        rm $O_LATEX/* -R
        
        
        TEXINPUTS=$LATEX:$LATEX/Pictures:$TEXINPUTS max_print_line=$max_width lualatex $flags_l presentation.tex -draftmode >/dev/null
        # bibtex file
        # makeindex file.idx # if needed
        # makeindex -s style.gls ... # glossary
        TEXINPUTS=$LATEX:$LATEX/Pictures:$TEXINPUTS max_print_line=$max_width lualatex $flags_l presentation.tex -draftmode >/dev/null
        
        TEXINPUTS=$LATEX:$LATEX/Pictures:$TEXINPUTS max_print_line=$max_width lualatex $flags_l presentation.tex | Echo 
        
        /mnt/c/Program\ Files/Adobe/Acrobat\ DC/Acrobat/Acrobat.exe $O_LATEX/presentation.pdf &
fi


plaats "Simulatie-tijd"
    print_hfill "$t0 -\> $(date +$FormatDate):" "$(date -d@$SECONDS -u +%Hh\ %Mm\ %Ss)"

cp $log_file $O_LOGS/$t0.log