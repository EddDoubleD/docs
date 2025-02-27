* **Client output buffer limit normal**{#settings-limit-normal}{{ tag-all }}

   Setting a limit on the output buffer for regular clients.

   {{ RD }} uses an output buffer to store data generated by a query before sending it out to a client. If a client is sending new queries faster than {{ RD }} can process pending ones, this causes the buffer to grow.

   This setting includes the following parameters:

   * **Hard limit**: Hard buffer size limit (in bytes). If this value is exceeded, the connection with the client will terminate immediately. The minimum value is `0` (no limit). The default value is `0`. In the management console, you define units of measurement using the **Hard limit unit** parameter.
   * **Soft limit**: Soft buffer size limit (in bytes). The connection to the client will not terminate unless this value is exceeded for a period of time specified in the **Soft seconds** parameter. The minimum value is `0` (no limit). The default value is `0`. In the management console, you define units of measurement using the **Soft limit unit** parameter.
   * **Soft seconds**: Time (seconds) for which soft buffer limit may be exceeded. The minimum value is `0`. The default value is `0`.

   For more information about this setting, see the [{{ RD }} documentation](https://redis.io/docs/reference/clients/#output-buffer-limits).

* **Client output buffer limit pubsub**{#settings-limit-pubsub}{{ tag-all }}

   This limits the output buffer size for clients using the [Pub/Sub](https://redis.io/docs/manual/pubsub/) pattern.

   {{ RD }} uses an output buffer to store data generated by a query before sending it out to a client. If a client is sending new queries faster than {{ RD }} can process pending ones, this causes the buffer to grow.

   This setting includes the following parameters:

   * **Hard limit**: Hard buffer size limit (in bytes). If this value is exceeded, the connection with the client will terminate immediately. The minimum value is `0` (no limit). The default value is `33554432` (32 MB). In the management console, you define units of measurement using the **Hard limit unit** parameter.
   * **Soft limit**: Soft buffer size limit (in bytes). The connection to the client will not terminate unless this value is exceeded for a period of time specified in the **Soft seconds** parameter. The minimum value is `0` (no limit). The default value is `8388608` (8 MB). In the management console, you define units of measurement using the **Soft limit unit** parameter.
   * **Soft seconds**: Time (seconds) for which soft buffer limit may be exceeded. The minimum value is `0`, while the default one is `60`.

   For more information about this setting, see the [{{ RD }} documentation](https://redis.io/docs/reference/clients/#output-buffer-limits).

* **Databases**{#settings-databases} {{ tag-all }}

   Number of databases.

   {{ RD }} uses the concept of logical databases isolated from one another. Operations with keys and values in one database do not affect data in other databases. Each database is identified by its own number (from `0` to `Databases − 1`).

   The minimum value is `0`, the maximum one is `2147483647`, and the default one is `16`.

   For more information, see the [{{ RD }} documentation](https://github.com/redis/redis/blob/6.0/redis.conf#L275).

   {% note warning %}

   If you change this parameter, all running {{ RD }} nodes will be restarted.

   {% endnote %}

* **Maxmemory policy**{#settings-maxmemory-policy} {{ tag-all }}

   This defines the memory management mode when there is not enough memory.

   * `volatile-lru`: Delete keys whose TTL has expired, starting with the least recently used (LRU) key.
   * `volatile-lfu`: Delete expired keys, starting with the least frequently used (LFU) key.
   * `volatile-ttl`: Delete expired keys, starting with the key with the lowest TTL.
   * `volatile-random`: Delete expired keys in random order.
   * `allkeys-lru`: Delete keys regardless of their TTL, starting with the least recently used one.
   * `allkeys-lfu`: Delete keys regardless of their TTL, starting with the least frequently used one.
   * `allkeys-random`: Delete keys in any order regardless of their TTL.
   * `noeviction` (default): Do not delete keys. Return an error if there is not enough memory to insert the data.

   For more information, see the [{{ RD }} documentation](https://docs.redislabs.com/latest/rs/administering/database-operations/eviction-policy/).

* **Notify keyspace events**{#settings-notify-keyspace-events} {{ tag-all }}

   This setting configures notifications about keyspace events.

   Its value is a string with modifiers that manage notification output. The default value is an empty string (notification output is disabled).

   For a complete list of modifiers, see the [{{ RD }} documentation](http://redis.io/topics/notifications).

* **Slowlog log slower than**{#settings-slowlog-slower-than} {{ tag-all }}

   Queries that run longer than the specified time (in microseconds) are considered slow. These queries are logged to the slow log. If the value is `0`, all queries being run are logged there.

   The minimum value is `-1` (there is no slow log), the maximum one is `9223372036854775807`, and the default one is `10000`.

   For more information, see the [{{ RD }} documentation](https://redis.io/commands/slowlog).

* **Slowlog max len**{#settings-slowlog-max-len} {{ tag-all }}

   Maximum number of entries in the slow query log. When the log is at its maximum length, before inserting new entries, the oldest ones will be removed.

   The minimum value is `0` (there is no slow log), the maximum one is `9223372036854775807`, and the default one is `1000`.

   For more information, see the [{{ RD }} documentation](https://redis.io/commands/slowlog).

* **Timeout**{#settings-timeout} {{ tag-all }}

   The time (in seconds) during which a connection to an inactive client is maintained.

   The minimum and default value is `0` (connections are not terminated), while the maximum one is `2147483647`.

   For more information, see the [{{ RD }} documentation](https://redis.io/topics/clients).
