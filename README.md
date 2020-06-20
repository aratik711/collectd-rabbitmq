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

#### Additionally I have modified the code to send the. following metrics as well.
## Nodes
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
