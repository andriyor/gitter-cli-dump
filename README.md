# gitter-cli-dump

> Export a JSON archive of a Gitter room's messages


## Usage

Use `--token` or specify `GITTER_TOKEN` env variable to authenticate.

You can find your Gitter token by logging into [https://developer.gitter.im/login](https://developer.gitter.im/login).

### List user's rooms

```
❯ python gitter_cli.py --room list  
```

The above command shows the user's rooms and its ids

### Export room

```
❯ python get_toom_list.py --dump <room_id> > file_name.json
```

The above command will dump a bunch of JSON to STDOUT with progress to STDERR.  Redirect to file if you wish.
