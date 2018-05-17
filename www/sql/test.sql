/*
 * File: /Users/wanghui/Documents/Python_Workspace/awesome-python3-webapp/www/test.sql
 * Project: /Users/wanghui/Documents/Python_Workspace/awesome-python3-webapp/www
 * Created Date: Thursday, May 17th 2018, 11:51:24 pm
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






SELECT * FROM awesome.users LIMIT 1000;

INSERT INTO `awesome`.`users` (`id`, `email`, `passwd`, `admin`, `name`, `create_at`) VALUES ('1', 'www@www.com', '111', '1', 'www', '111');
INSERT INTO `awesome`.`users` (`id`, `email`, `passwd`, `admin`, `name`, `create_at`) VALUES ('2', 'mmm@mmm.com', '222', '0', 'mmm', '222');