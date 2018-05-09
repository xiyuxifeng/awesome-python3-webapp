/*
 * File: /Users/wanghui/Documents/Python_Workspace/awesome-python3-webapp/www/db.sql
 * Project: /Users/wanghui/Documents/Python_Workspace/awesome-python3-webapp/www
 * Created Date: Wednesday, May 9th 2018, 11:20:28 pm
 * Author: Wang Hui
 * -----
 * Last Modified:
 * Modified By:
 * -----
 * Copyright (c) 2018 WH
 *
 * All shall be well and all shall be well and all manner of things shall be well.
 * We're doomed!
 */

drop database if EXISTS awesome;

create database awesome;

use awesome;

-- 1. 创建本地用户bm_user, 密码为 password
-- 2. 将bookmarks数据库下的所有表的查询，修改，删除权限授予该用户

grant select, insert, update, delete on awesome.* to 'python'@'localhost' identified by 'python';


create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500),
    `create_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500),
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `create_at` real not null,
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500),
    `content` mediumtext not null,
    `create_at` real not null,
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;