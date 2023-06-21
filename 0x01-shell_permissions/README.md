# SHELL PERMISSIONS

In shell we have a very tight environment, hence everyone has to be permitted before he is allowed to do anything. Except the ``root`` well because he's the root. Although commands like ``sudo`` and ``su`` may give us leeway once a while but it's often more advised to set permissions to allow the **user**, **group** and **other users** know what to do with a file. the basic permissions are ``rwx``

* ``r`` allows those permitted to view the file. this is one of the most common permissions
* ``w`` allows those permitted to edit the file. This is less common
* ``x`` allows those permitted to execute the file.

## Files :notebook:

|Files|Purpose|Type|
|:---|:---|:---:|
|[_hello](./_hello)|Just a text file|``text file``|
|[0-iam_betty](./0-iam_betty)|this swithes the currect user to betty|``Shell``|
|[1-who_am_i](./1-Thiswho_am_i)|This script prints the effective username of the current user|``Shell``|
|[2-groups](./2-groups)|This script prints all the groups the current user is part of|``Shell``|
|[3-new_owner](./3-new_owner)|This changes the owner of the file hello to ``betty``|``Shell``|
|[4-empty](./4-empty)|This creates an empty file called hello|``Shell``|
|[5-execute](./5-execute)|This adds the execute permision to the owner of hello only|``Shell``|
|[6-multiple_permissions](./6-multiple_permissions)|This adds</br> execute permision to the owner</br>  execute permision to the group owner of hello</br>read permission to other users of hello|``Shell``|
|[7-everybody](./7-everybody)|This adds  execution permisson to the owner, group owner and other users of the file hello|``Shell``|
|[8-Jamesond](./8-James_Bond)|This sets the permission of the file ``hello`` as follows</br>owner no permission</br>group no permission</br>other users all permissions|``Shell``|
|[9-John_Doe](./9-John_Doe)|This sets the mode of hello to</br>``-rwxr-x-wx 1 julien julien 23 sep 2 0 14:25 hello``|``Shell``|
|[10-mirror_permissions](./10-mirror_permissions)|This sets the mode of ``hello`` to that ofthe file ``olleh``. Both files will be present in the working directory|``Shell``|
|[11-directories_permissions](./11-directories_permissions)|This adds execute permission to all sub directories of current directory for everyone only. Regular files are not affected|``Shell``|
|[12-directory_permissions](./12-directory_permissions)|This creates the directory ``my_dir`` with permissions ``751``|``Shell``|
|[13-change_group](./13-change_group)|This changes the group owner of the file ``hello`` to ``school``|``Shell``|
|[100-change_owner_and_group](./100-change_owner_and_group)|This changes owner to ``vincent`` and group owner to ``staff`` for the current directory and everything in it|``Shell``|
|[101-symbolic_link_permissions](./101-symbolic_link_permissions)|This changes te owner and group owner of ``_hello`` to ``vincent`` and ``staff``. _hello is a symlink|``Shell``|
|[102-if_only](./102-if_only)|This changes owner of the file ``hello`` to ``betty`` if it is owned by ``guillaume``|``Shell``|
|[103-Star_Wars](./103-Star_Wars)|This script plays Star Wars IV episode in the terminal|``Shell``|
