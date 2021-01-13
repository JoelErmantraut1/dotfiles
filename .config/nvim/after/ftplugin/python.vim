" Configuracion de Kite
map <leader>gd :KiteGotoDefinition<CR>
map <leader>kk :KiteDocsAtCursor<CR>
inoremap <c-p> <C-x><C-u>

set completeopt+=menuone
set completeopt+=noselect
set completeopt+=preview
autocmd CompleteDone * if !pumvisible() | pclose | endif
set belloff+=ctrlg  " if vim beeps during completion

nnoremap <leader>b :sp <CR> :term python % <CR>
