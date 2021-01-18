call plug#begin(stdpath('config') . '/plugged')

" Themes 
Plug 'sainnhe/sonokai'
Plug 'jacoborus/tender.vim'

" Files 
Plug 'preservim/nerdtree' " NERDTree
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'

" Syntaxis
Plug 'frazrepo/vim-rainbow' " Shows rainbow brackets and others 
Plug 'preservim/nerdcommenter' " Comments Code
Plug 'nathanaelkane/vim-indent-guides' " See guides identation 
Plug 'chrisbra/colorizer' " Shows colors with colors 

" Syntax Highlighting
Plug 'digitaltoad/vim-pug'
Plug 'cakebaker/scss-syntax.vim'
Plug 'vim-python/python-syntax'

" Interfaz
Plug 'itchyny/lightline.vim' " Status Bar 
Plug 'KabbAmine/vCoolor.vim' " Color Selector
Plug 'wfxr/minimap.vim' " Sublime-text minimap style
Plug 'voldikss/vim-floaterm'

" Codificacion
Plug 'majutsushi/tagbar'
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Search in code 
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Autocompletion 
" Installed with Coc: coc-prettier and coc-pairs

call plug#end()
