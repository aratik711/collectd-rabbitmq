# Collectd Rabbitmq

This repository is an enhanced version of the collectd-rabbitmq plugin
[https://github.com/nytimes/collectd-rabbitmq](https://github.com/nytimes/collectd-rabbitmq)

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
