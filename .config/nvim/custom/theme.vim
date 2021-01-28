set termguicolors

syntax enable
"colorscheme ayu
"colorscheme sonokai 
colorscheme tender 
"colorscheme nord 
"colorscheme gruvbox

"let ayucolor="dark"  " for light version of theme

" The idea (testing) is that each file would have a different theme.
"let ftToIgnore = ['python', 'html', 'css', 'javascript', 'c', 'cpp']

"autocmd BufWritePre * if index(ftToIgnore, &ft) < 0 | SetAllOption()
"autocmd Filetype * call SetAllOption()
"autocmd Filetype python call SetPythonOptions()
"autocmd Filetype html,css,javascript call SetWebOptions()
"autocmd Filetype c,cpp call SetClangOptions()

"function SetPythonOptions()
    "colorscheme tender
"endfunction

"function SetWebOptions()
    "colorscheme gruvbox
"endfunction

"function SetClangOptions()
    "colorscheme nord 
"endfunction

"function SetAllOption()
    "colorscheme sonokai
"endfunction

highlight ColoColumn ctermbg=0 guibg=lightgrey
