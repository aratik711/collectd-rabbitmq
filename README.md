# Collectd Rabbitmq

This repository is an enhanced version of the collectd-rabbitmq plugin
[https://github.com/nytimes/collectd-rabbitmq](https://github.com/nytimes/collectd-rabbitmq)

#### The following metrics are sent by the above mentioned plugin
## Nodes

For each node the following statistics are gathered:

-   disk_free_limit
-   fd_total
-   fd_used
-   mem_limit
-   mem_used
-   proc_total
-   proc_used
-   processors
-   run_queue
-   sockets_total
-   sockets_used

## Queues

For each queue in each vhost the following statistics are gathered: _NOTE_: The / vhost name is sent as default

-   message_stats
	-	deliver_get
    -   deliver_get_details
        
        -   rate
        
    -   get
    -   get_details
        
        -   rate
        
    -   publish
    -   publish_details
        
        -   rate
        
    -   redeliver
    -   redeliver_details
        
        -   rate
        
    
-   messages
-   messages_details
    
    -   rate
    
-   messages_ready
-   messages_ready_details
    
    -   rate
    
-   messages_unacknowledged
-   messages_unacknowledged_details * rate
-   memory
-   consumers
-   consumer_utilisation

## Exchanges

For each exchange in each vhost the following statistics are gathered: _NOTE_: The / vhost name is sent as default

-   disk_free
-   disk_free_limit
-   fd_total
-   fd_used
-   mem_limit
-   mem_used
-   proc_total
-   proc_used
-   processors
-   run_queue
-   sockets_total
-   sockets_used

#### Additionally I have modified the code to send the following metrics as well.
## Queues
- gc_num
- gc_bytes_reclaimed
- context_switches
- io_write_bytes
- io_read_count
- io_read_bytes
- io_read_avg_time
- io_write_count
- io_write_avg_time
- io_sync_count
- io_sync_avg_time
- io_seek_count
- io_seek_avg_time
- io_reopen_count
- mnesia_ram_tx_count
- mnesia_disk_tx_count
- msg_store_read_count
- msg_store_write_count
- queue_index_journal_write_count
- queue_index_write_count
- queue_index_read_count
- io_file_handle_open_attempt_count
- io_file_handle_open_attempt_avg_time
- connection_created
- connection_closed
- channel_created
- channel_closed
- queue_declared
- queue_created
- queue_deleted
- gc_num_details
	- rate
- gc_bytes_reclaimed_details
	- rate
- context_switches_details
	- rate
- io_write_bytes_details
	- rate
- io_read_count_details
	- rate
- io_read_bytes_details
	- rate
- io_read_avg_time_details
	- rate
- io_write_count_details
	- rate
- io_write_avg_time_details
	- rate
- io_sync_count_details
	- rate
- io_sync_avg_time_details
	- rate
- io_seek_count_details
	- rate
- io_seek_avg_time_details
	- rate
- io_reopen_count_details
	- rate
- mnesia_ram_tx_count_details
	- rate
- mnesia_disk_tx_count_details
	- rate
- msg_store_read_count_details
	- rate
- msg_store_write_count_details
	- rate
- queue_index_journal_write_count_details
	- rate
- queue_index_write_count_details
	- rate
- queue_index_read_count_details
	- rate
- io_file_handle_open_attempt_count_details
	- rate
- io_file_handle_open_attempt_avg_time_details
	- rate
- connection_created_details
	- rate
- connection_closed_details
	- rate
- channel_created_details
	- rate
- channel_closed_details
	- rate
- queue_declared_details
	- rate
- queue_created_details
	- rate
- queue_deleted_details
	- rate

The above metrics will be sent in `<node-name>_value` measurement.
## Memory
These metrics are pulled from the `/api/nodes/<NODENAME>/memory` api. 
The raw respoonse from the above api is as:
```json
{
   "memory":{
      "connection_readers":69440,
      "connection_writers":3264,
      "connection_channels":11560,
      "connection_other":492588,
      "queue_procs":243852,
      "queue_slave_procs":14480,
      "plugins":3479384,
      "other_proc":23210812,
      "metrics":236636,
      "mgmt_db":2121208,
      "mnesia":152968,
      "other_ets":3026016,
      "binary":578656,
      "msg_index":86848,
      "code":24176580,
      "atom":1180881,
      "other_system":11801659,
      "allocated_unused":11291216,
      "reserved_unallocated":5120000,
      "strategy":"rss",
      "total":{
         "erlang":70886832,
         "rss":87298048,
         "allocated":82178048
      }
   }
}
```
The below metrics are sent:
- default
	- connection_readers
	- connection_writers
	- connection_channels
	- connection_other
	- queue_procs
	- queue_slave_procs
	- plugins
	- other_proc
	- metrics
	- mgmt_db
	- mnesia
	- other_ets
	- binary
	- msg_index
	- code
	- atom
	- other_system
	- allocated_unused
	- reserved_unallocated
- total
	- rss
	- erlang
	- allocated

These metrics are sent to `nodememory_value` measurement.	This will also contain the FQDN of the node in the `host` tag.

### Changes
The other changes made to the plugin are:
 1. In `queues_value` the value for `host` tag was the vhost name, I needed the value of the RMQ host to be added to this measurement as well, so the format of `host` has been changed to `vhost@hostname`.
 So if the vhost was `/` and FQDN of the RMQ node was `rmq-test001.prod`, the host value would be `rabbitmq_default@rmq-test001.prod`

### How to use:
To use this code, please follow the below mentioned steps:
1. Install `collectd`, ``libpython2.7``, ``libatlas3-base``. 
2. Clone the repository
``` 
git clone git@github.com:aratik711/collectd-rabbitmq.git
```
3. Copy the directory collectd-rabbitmq/collectd-rabbitmq to the PYTHONPATH
``` 
cp -r collectd-rabbitmq/collectd-rabbitmq /usr/local/lib/python2.7/dist-packages
```
4. Copy the `rabbitmq.types.db` to `/usr/share/collectd/` with 644 read/write permissions.
5. Add a collectd config for rabbitmq `/etc/collectd/collectd.conf.d/rabbitmq.conf` with 644 read/write permissions.
```
TypesDB "/usr/share/collectd/rabbitmq.types.db"
TypesDB "/usr/share/collectd/types.db"
<LoadPlugin "python">
    Globals true
</LoadPlugin>

<Plugin "python">

    LogTraces true
    Interactive false
    Import "collectd_rabbitmq.collectd_plugin"
    <Module "collectd_rabbitmq.collectd_plugin">

      Username "monuser"
      Password "mypass"
      Realm "RabbitMQ Management"
      Host "rmq-test001.prod"
      Port "15672"
    </Module>
</Plugin>
```
6. Create a monitoring user and give it login rights to all the vhosts.
```bash
#!/bin/bash
rabbitmqctl add_user monuser mypass
rabbitmqctl set_user_tags monuser monitoring
for vhost in $(rabbitmqctl list_vhosts -q | grep -v name); do
 echo $vhost
 rabbitmqctl set_permissions -p $vhost "monuser" "" "" ""
done
```
7. Restart collectd `service collectd restart`. The metrics should start coming in, in your data source.

### Debugging
In case you want to print the logs. You can add the following in `collectd.conf` file:
```
LoadPlugin logfile
<Plugin logfile>
        LogLevel info
        File "/var/log/collectd.log"
        Timestamp true
        PrintSeverity true
</Plugin>
```
Makesure it is added before any other Plugin entry. Restart the collectd service and logs should be streaming in.
