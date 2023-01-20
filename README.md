# TAGALONG

Simply add tags to folders to keep track what you're currently working on in
which folder.

## Why?

If you work on projects that build specific configurations and where the build
takes a long time to finish and where the sources are quiet big, its not very
practical to use git to switch branches, because the built artifacts might not
correspond to the given sources. Also, I don't want to mess with my git
branches to tag my current work. So, why not just naming the folder
accordingly? Re-naming the folder might break automatically generated build
artifacts that expand the path to the current folder. Imagine, e.g., juggeling
around several buildroot compilations (with different options enabled and with
different targets). Here, it becomes practial to flag a folder with which setup
the given sources are for.

## How?

The tool consists of a mere 70 lines of Python code and stores all tags for
each folder in a json based database in `~/.config/tagalong/tagalong_db.json`.
The database is human readable and can be opend with a simple texteditor. So,
if you ever messed up your tags you can simply edit the file and correct it (or
delete the whole database if you don't need the tags anymore). Each database
entry juste consists of a folder property and a tags property. The folder
property returns a folder path as a string, and the tags property returns a
list with all the tags associated with a given folder.

## I want to try it!

Get the dependencies:

* Python3 (`apt install python3`)
* TinyDB (`pip3 install tinydb`)

Then clone the repository:

```
git clone git@github.com:deathjest3r/tagalong.git
```

Then add aliases to your `~/.zshrc` to simply add or remove a tag from the
current working directory:

```
alias tag='() { <path-to-tagalong-clone>/tagalong.py -a ${1} `pwd` ;}'
alias untag='() { if [[ ! -z ${1} ]] then <path-to-tagalong-clone>/tagalong.py -d ${1}; else <path-to-tagalong-clone>/tagalong.py -u; fi ;}'
```

With a simple
```
tag my_fancy_tag
```
the current folder can be tagged with the tag `my_fancy_tag`. If no argument is
given to the untag command, all tags will be removed from the current folder.

The tags of a given folder can be shown with `./tagalong.py <folder-name>`. But
to make the whole thing useful, it needs to be added to your zsh prompt, to
show the tags of the current folder, just like the current git branch. When
using e.g., the `robbyrussel.zsh-theme` from
[oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh/) the folder tags can be added
to the prompt in the following way:

```
-PROMPT+=' %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)'
+PROMPT+=' %{$fg[cyan]%}%c%{$reset_color%} %{$fg_bold[blue]%}tags:(%{$fg[red]%}$(<path-to-tagalong-clone>/tagalong.py `pwd`)%{$fg_bold[blue]%}) $(git_prompt_info)'
```

Afterwards the prompt looks like:
![tagalong_example](https://user-images.githubusercontent.com/1267671/210577884-01f272f0-9c57-4d80-9c6c-f22836b8d40d.png)
