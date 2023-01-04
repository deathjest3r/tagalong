# TAGALONG

Simply add tags to folder to keep track what you're currently working on in
which folder.

## Why?

If you work on projects that build (where the build takes a long time to
finish) specific configurations, its not very practical to use git to switch
branches, because the built artifacts might not correspond to the given
sources. So, why not just naming the folder accordingly? Re-naming the folder
might break automatically generated build artifacts that expand the path to the
current folder. Imagine, e.g., juggeling around several buildroot compilations
(with different options enabled and with different targets). Here, it becomes
practial to flag a folder with which setup the given sources are for.

## How?

First clone the repository:

```
git clone git@github.com:deathjest3r/tagalong.git

```

Then ddd aliases to your `~/.zshrc` to simply add or remove a tag from the
current working directory:

```
alias tag='() { <path-to-tagalong-clone>/tagalong.py -a ${1} `pwd` ;}'
alias untag='() { <path-to-tagalong-clone>/tagalong.py -d ${1} `pwd` ;}'
```

With a simple
```
tag my_fancy_tag
```
the current folder can be tagged with the tag `my_fancy_tag`.

The tags of a given folder can be shown with `./tagalong.py <folder-name>`. But
to make the whole thing useful, it needs to be added to your zsh prompt, to
show the tags of the current folder, just like the current git branch. When
using e.g., the `robbyrussel.zsh-theme` from
[oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh/) the folder tags can be added
to the prompt in the following way:

```
-PROMPT+=' %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)'
+PROMPT+=' %{$fg[cyan]%}%c%{$reset_color%} %{$fg_bold[blue]%}tags:(%{$fg[red]%}$(/work1/tagalong/tagalong.py `pwd`)%{$fg_bold[blue]%}) $(git_prompt_info)'
```
