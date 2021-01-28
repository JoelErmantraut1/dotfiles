call plug#begin(stdpath('config') . '/plugged')

" Themes 
Plug 'sainnhe/sonokai'
Plug 'jacoborus/tender.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'ayu-theme/ayu-vim'
Plug 'morhetz/gruvbox'

" Files 
Plug 'preservim/nerdtree' " NERDTree
Plug 'ryanoasis/vim-devicons'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'
Plug 'jeetsukumaran/vim-buffergator' " To manage buffers

" Syntaxis
Plug 'frazrepo/vim-rainbow' " Shows rainbow brackets and others 
Plug 'preservim/nerdcommenter' " Comments Code
Plug 'chrisbra/colorizer' " Shows colors with colors 

" Syntax Highlighting
Plug 'digitaltoad/vim-pug'
Plug 'cakebaker/scss-syntax.vim'
Plug 'vim-python/python-syntax'

" Interfaz
Plug 'itchyny/lightline.vim' " Status Bar 
Plug 'KabbAmine/vCoolor.vim' " Color Selector
Plug 'voldikss/vim-floaterm'
Plug 'mhinz/vim-startify' " Start screen
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
"Plug 'Yggdroot/indentLine' " Indent line

" Codificacion
Plug 'majutsushi/tagbar'
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Search in code 
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Autocompletion 
Plug 'itchyny/vim-gitbranch' " To show git branch in status bar
Plug 'airblade/vim-gitgutter' " To show changes in file
" Installed with Coc: coc-prettier and coc-pairs

call plug#end()
