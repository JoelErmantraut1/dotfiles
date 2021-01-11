call plug#begin(stdpath('config') . '/plugged')

" Temas
Plug 'sainnhe/sonokai'

" Archivos
Plug 'preservim/nerdtree' " NERDTree
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'

" Sintaxis
Plug 'frazrepo/vim-rainbow' " Muestra parentesis de colores
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Auto completado de muchos lenguajes
Plug 'preservim/nerdcommenter' " Comentado de codigo
Plug 'nathanaelkane/vim-indent-guides' " Para ver las guias de la indentacion
Plug 'jiangmiao/auto-pairs' " Cierra parentesis, corchetes, etc
Plug 'digitaltoad/vim-pug' " Sintaxis para Pug
Plug 'cakebaker/scss-syntax.vim' " Sintaxis para Sass
Plug 'dense-analysis/ale' " ALE: Tiene muchas funciones, pero uso Lint y Fix
Plug 'chrisbra/colorizer' " Remarca con el color de esta escrito
" Plug 'vim-python/python-syntax' " Sintaxis para Python

" Interfaz
Plug 'itchyny/lightline.vim' " Muestra el status con colores
Plug 'KabbAmine/vCoolor.vim' " Hace aparecer un selector de colores
Plug 'wfxr/minimap.vim' " Sublime-text minimap style

" Codificacion
Plug 'majutsushi/tagbar' " Organizacion del codigo
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Busqueda y locacion de caracteres

call plug#end()
