syntax on " Activa la sintaxis
set number " Muestra en que linea estamos
set mouse=a " Interactuar con el mouse
set noerrorbells " No de sonidos de error
set sw=4 " Tamaño del tab
set expandtab " Los tabs son espacios
set tabstop=4
set softtabstop=4
set smartindent " Tabulacion inteligente
set numberwidth=1 " Optimiza del espacio a la izquierda
set nobackup
set nowritebackup
set nowrap
set incsearch " Va mostrando resultados a medida que busca
set ignorecase " Ignora las mayusculas en la busqueda
set encoding=utf-8
set cursorline
set termguicolors
set colorcolumn=80 " Para que aparezca la linea que marca el limite
set nolist
set updatetime=10 " Aumenta la frecuencia de actualizacion
set timeoutlen=500 " Coloca el tiempo de espera de la leader key
set hidden
set clipboard=unnamed
filetype plugin on
highlight ColoColumn ctermbg=0 guibg=lightgrey

" PLUGINS

call plug#begin('~/.config/nvim/plugged')

" Temas
Plug 'sainnhe/sonokai'

" Archivos
Plug 'preservim/nerdtree' " NERDTree
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF

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
Plug 'vim-python/python-syntax' " Sintaxis para Python

" Interfaz
Plug 'itchyny/lightline.vim' " Muestra el status con colores
Plug 'KabbAmine/vCoolor.vim' " Hace aparecer un selector de colores
Plug 'wfxr/minimap.vim' " Sublime-text minimap style

" Codificacion
Plug 'majutsushi/tagbar' " Organizacion del codigo
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Busqueda y locacion de caracteres

call plug#end()

" HOTKEYS

let mapleader = " "
" Tecla modificadora (leader)

" Generales
nnoremap <leader>s :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>qq :q!<CR>
nnoremap <leader>fs :Files<CR>
nnoremap <leader>u :UndotreeShow<CR>

" Redimensiona las pestañas
nnoremap <silent> <Left> :vertical resize +2<CR> 
nnoremap <silent> <Up> :resize -2<CR>
nnoremap <silent> <Down> :resize +2<CR>
nnoremap <silent> <Right> :vertical resize -2<CR>

" Tab Control
nnoremap <leader>d :bnext<CR>
nnoremap <leader>a :bprevious<CR>
nnoremap <leader>w :bdelete<CR>
" Splits
nnoremap <leader>vs :vsp<space>
nnoremap <leader>sp :sp<space>
" Windows
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" Alterar sintaxis
vnoremap <expr> p '"_d"'.v:register.'p'
vnoremap <expr> P '"_d"'.v:register.'P'

" Escribe el comando, si le das ENTER te abre el mismo
" archivo en otra pestaña

" Vim Rainbow
let g:rainbow_active = 1

" Configuracion de Kite
let g:kite_supported_languages = ['javascript', 'python']
let g:kite_tab_complete=1

fun! GoKite()
    " Configuracion de Kite
    map <leader>gd :KiteGotoDefinition<CR>
    map <leader>k :KiteDocsAtCursor<CR>
    inoremap <c-p> <C-x><C-u>

    set completeopt+=menuone
    set completeopt+=noselect
    set completeopt+=preview
    autocmd CompleteDone * if !pumvisible() | pclose | endif
    set belloff+=ctrlg  " if vim beeps during completion
endfun

" Configuracion de CoC
fun! GoCoc()
    function! s:check_back_space() abort
      let col = col('.') - 1
      return !col || getline('.')[col - 1]  =~# '\s'
    endfunction
    inoremap <buffer> <silent><expr> <TAB>
          \ pumvisible() ? "\<C-n>" :
          \ <SID>check_back_space() ? "\<TAB>" :
          \ coc#refresh()
    inoremap <buffer> <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"
    inoremap <buffer> <silent><expr> <C-space> coc#refresh()

    nmap <leader>gd <Plug>(coc-definition)
    nmap <leader>gt <Plug>(coc-type-definition)
    nmap <leader>gi <Plug>(coc-implementation)
    nmap <leader>gr <Plug>(coc-references)
    nnoremap <buffer> <leader>cr :CoCRestart

    " Highlight the symbol and its references when holding the cursor.
    autocmd CursorHold * silent call CocActionAsync('highlight')
endfun

" Seleccion de herramienta de autocompletado
autocmd FileType python :call GoKite()
autocmd FileType html,css,javascript :call GoCoc()

" Ejecucion de archivos
autocmd FileType python nnoremap <leader>b :sp <CR> :term python % <CR>
autocmd FileType c nnoremap <leader>b :sp<CR> :term gcc % -o %< && ./%< <CR>

" Configuracion de NERDTree
let g:NERDTreeChDirMode = 1 " Cambia el directorio actual al nodo padre actual
map <leader>n :NERDTreeToggle<CR>

" Configuracion de NERDCommenter
let g:NERDCreateDefaultMappings = 0
let g:NERDSpaceDelims = 1
nnoremap <leader>c :call NERDComment(0,"toggle")<CR>
vnoremap <leader>c :call NERDComment(0, "toggle")<CR>

" Configuracion de Emmet
let g:user_emmet_leader_key='<C-X>'
" La combinacion va a ser Ctrl+ X + ,
let g:user_emmet_mode='a'    "only enable normal mode functions.
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstall

" Configuracion de Tagbar
nmap <leader>t :TagbarToggle<CR>

" Configuracion de MiniMap
nmap <leader>mm :MinimapToggle<CR>

" Configuracion de EasyMotion
map  / <Plug>(easymotion-sn)
omap / <Plug>(easymotion-tn)
nnoremap <leader>7 :noh<CR>
let g:EasyMotion_smartcase = 1
" Con esto v encuentra v y V, pero V solo encuentra V

" Configuracion de ALE
let g:ale_fixers = ['prettier']
let g:ale_fix_on_save_ignore=1
nnoremap <leader>e :ALEFix<CR>

nnoremap <leader>r :ColorHighlight<CR>
" Remarca los colores del texto

" Python Sintaxis
let g:python_highlight_all = 1

" INICIALIZACION

" Configuracion de LightLine
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'charvalue' ] ],
      \   'right': [ [ 'kitestatus', 'coc-status', 'fileencoding', 'filetype', 'percent', 'lineinfo' ] ]
      \ },
      \ 'component': {}
      \ }

colorscheme sonokai

" Configuracion de IndentGuides
" let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_guide_size = 1
let g:indent_guides_exclude_filetypes = ['help', 'nerdtree']
let g:indent_guides_default_mapping = 0
