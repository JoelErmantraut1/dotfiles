call plug#begin(stdpath('config') . '/plugged')

" Themes 
Plug 'sainnhe/sonokai'

" Files 
Plug 'preservim/nerdtree' " NERDTree
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'
Plug 'dbeniamine/cheat.sh-vim' " To search in cht.sh directly from vim

" Syntaxis
Plug 'frazrepo/vim-rainbow' " Shows rainbow brackets and others 
Plug 'preservim/nerdcommenter' " Comments Code
Plug 'nathanaelkane/vim-indent-guides' " See guides identation 
Plug 'neoclide/coc-pairs', {'branch': 'release'}
Plug 'neoclide/coc-eslint', {'branch': 'release'}
Plug 'neoclide/coc-prettier', {'branch': 'release'}
Plug 'chrisbra/colorizer' " Shows colors with colors 
" Plug 'jiangmiao/auto-pairs' " Cierra parentesis, corchetes, etc
" Plug 'dense-analysis/ale' " ALE: Tiene muchas funciones, pero uso Lint y Fi

" Syntax Highlighting
Plug 'digitaltoad/vim-pug'
Plug 'cakebaker/scss-syntax.vim'
Plug 'vim-python/python-syntax'

" Interfaz
Plug 'itchyny/lightline.vim' " Status Bar 
Plug 'KabbAmine/vCoolor.vim' " Color Selector
Plug 'wfxr/minimap.vim' " Sublime-text minimap style

" Codificacion
Plug 'majutsushi/tagbar'
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Search in code 
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Autocompletion 

call plug#end()
