#!/bin/bash

# Update a file in to all existing branches


BRANCHES=(
cms
cms_2_cli
cms_3_app_factory
cms_3_config_factory
cms_3_extension_factory
cms_4_blog
cms_5_jinja
cms_5_template_globals
cms_6_static
cms_7_wsgi
cms_8_test
)

# export SOUR=/tmp/requirements.txt
# export DEST=.
# export MESS=":hamster:"

for BRANCH in "${BRANCHES[@]}";
do
    git checkout $BRANCH;
    git stash;
    cp $SOUR $DEST;
    git commit -am $MESS;
    git push -u origin $BRANCH;
    git stash pop;
done



# Cherry Pick
# ORIGINALBRANCH=`git status | head -n1 | cut -c13-`
# git commit -m $1
# CHERRYCOMMIT=`git log -n1 | head -n1 | cut -c8-`
# for BRANCH in "${BRANCHES[@]}";
# do
#     git stash;
#     git checkout $BRANCH;
#     git cherry-pick $CHERRYCOMMIT;
#     git checkout $ORIGINALBRANCH;
#     git stash pop;
# done


