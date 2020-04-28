# qgbd
Quick Git Branch Deleter: because I spend too much time manually deleting git branches

# usage

![qgbd demo gif](https://github.com/shawkinsl/qgbd/raw/docs/qgbd_usage.gif)

1. install: `pip install git+https://github.com/shawkinsl/qgbd.git`
1. use: `qgbd` (arrow keys + space to navigate checkboxes)

```
shawkins@shawkins-VirtualBox:~/pubcode/qgbd$ qgbd
[?] Check to remove branch: 
   o master
   X user/shawkins/feature_x
   o user/shawkins/feature_x_backup
   X user/shawkins/feature_x_rebase_take2
   X user/shawkins/feature_x_rebased
   X user/shawkins/feature_x_rebased_take2
   X user/shawkins/were_all_these_branches_necessary
 > X user/shawkins/you_make_too_many_branches_my_dude

will run: "git branch -D user/shawkins/feature_x user/shawkins/feature_x_rebase_take2 user/shawkins/feature_x_rebased user/shawkins/feature_x_rebased_take2 user/shawkins/were_all_these_branches_necessary user/shawkins/you_make_too_many_branches_my_dude" 
ok? (y/n): y
Deleted branch user/shawkins/feature_x (was 782141a).
Deleted branch user/shawkins/feature_x_rebase_take2 (was 782141a).
Deleted branch user/shawkins/feature_x_rebased (was 782141a).
Deleted branch user/shawkins/feature_x_rebased_take2 (was 782141a).
Deleted branch user/shawkins/were_all_these_branches_necessary (was 782141a).
Deleted branch user/shawkins/you_make_too_many_branches_my_dude (was 782141a).

```