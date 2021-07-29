---
doctest-type: bash
---

The remote tests below require that sshd is running locally.

    $ ssh localhost true

## nested_op

Run locally:

    $ guild run nested_op DEVMODE=yes -y
    hello world
    ('flag:', True)
    goodbye!

Run remotely (localhost via ssh):

    $ guild run nested_op DEVMODE=yes --remote ssh:localhost -y
    Building package
    ...
    Initializing remote run
    Copying package
    ...
    Starting nested_op on localhost as ...
    hello world
    ('flag:', True)
    goodbye!
    Run ... stopped with a status of 'completed'

## root_op

Run locally:

    $ guild run root_op DEVMODE=yes -y
    hello world
    ('flag:', True)
    goodbye!


Run remotely (localhost via ssh):

    $ guild run root_op DEVMODE=yes --remote ssh:localhost -y
    Building package
    ...
    Initializing remote run
    Copying package
    ...
    Starting root_op on localhost as ...
    hello world
    ('flag:', True)
    goodbye!
    Run ... stopped with a status of 'completed'
