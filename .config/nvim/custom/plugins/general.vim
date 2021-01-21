" Vim Rainbow
let g:rainbow_active = 1

" NERDTree
let g:NERDTreeChDirMode = 1 " Cambia el directorio actual al nodo padre actual

autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" To close vim when NERDTree is the only buffer

" NERDCommenter
let g:NERDCreateDefaultMappings = 0
let g:NERDSpaceDelims = 0

" Emmet
let g:user_emmet_leader_key='<C-X>'
" Activated with Ctrl + X + ,

let g:user_emmet_mode='a' " only enable normal mode functions.
let g:user_emmet_install_global = 0

let g:EasyMotion_smartcase = 1
" v finds v and V, but V finds V only

let g:buffergator_viewport_split_policy="R"
let g:buffergator_autoupdate=1
let g:buffergator_split_size=50
let g:buffergator_sort_regime="basename"
let g:buffergator_show_full_directory_path=0
let g:buffergator_suppress_keymaps = 1
" Not use default plugin keymap

" Python Syntaxis
let g:python_highlight_all = 1

if !exists('g:undotree_WindowLayout')
    let g:undotree_WindowLayout = 4
endif

if !exists('g:undotree_SplitWidth')
    let g:undotree_SplitWidth = 30
endif

" IndentGuides
" let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_guide_size = 1
let g:indent_guides_exclude_filetypes = ['help', 'nerdtree']
let g:indent_guides_default_mapping = 0

let g:lightline = {
      \ 'colorscheme': 'tender',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'readonly', 'filename', 'charvalue' ] ],
      \   'right': [ ['gitbranch', 'fileencoding', 'filetype', 'percent', 'lineinfo' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'FugitiveHead'
      \ },
      \ }
