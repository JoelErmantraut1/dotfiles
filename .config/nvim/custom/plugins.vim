call plug#begin(stdpath('config') . '/plugged')

" Themes 
Plug 'sainnhe/sonokai'
Plug 'jacoborus/tender.vim'

" Files 
Plug 'preservim/nerdtree' " NERDTree
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'
Plug 'jeetsukumaran/vim-buffergator' " To manage buffers

" Syntaxis
Plug 'frazrepo/vim-rainbow' " Shows rainbow brackets and others 
Plug 'preservim/nerdcommenter' " Comments Code
Plug 'nathanaelkane/vim-indent-guides' " See guides identation 
Plug 'chrisbra/colorizer' " Shows colors with colors 
Plug 'tbastos/vim-lua'

" Syntax Highlighting
Plug 'digitaltoad/vim-pug'
Plug 'cakebaker/scss-syntax.vim'
Plug 'vim-python/python-syntax'

" Interfaz
Plug 'itchyny/lightline.vim' " Status Bar 
Plug 'KabbAmine/vCoolor.vim' " Color Selector
Plug 'voldikss/vim-floaterm'
Plug 'mhinz/vim-startify' " Start screen

" Codificacion
Plug 'majutsushi/tagbar'
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Search in code 
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Autocompletion 
Plug 'tpope/vim-fugitive' " Git integration
Plug 'airblade/vim-gitgutter' " To show changes in file
" Installed with Coc: coc-prettier and coc-pairs


call plug#end()
