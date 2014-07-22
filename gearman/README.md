GEARMAN, THE MISSING MANUAL
=========

SET UP [GEARMAN SERVER]
--

    brew install gearman

SET UP GEARMAN PYTHON WRAPPER
--
    sudo pip install gearman

GEARMAND LOCATION
--
    /usr/local/sbin/gearmand

PERSISTENT QUEUE WITH POSTGRESQL
--
To get Postgresql working you need to use the -q Postgeres command line option.
    
Below is a command line to get persistent queues working with Postgresql. This command line was run on Ubuntu 12.04 server, Postgresql version 9.1, and Gearman v 0.27.
    
    gearmand -L 127.0.0.1 –libpq-conninfo ‘hostaddr=127.0.0.1 port=5432 dbname=gearman user=postgres’ –libpq-table=queue123 –verbose DEBUG -q Postgres

Also note: gearmand will create the table if it does not already exist. In the case above, it will crate a table named queue123

WORKER MANAGEMENT WITH [SUPERVISORD]
--
[TO BE WORKED ON]

MONITORING WITH [GEARMAN UI]
--
- DEPENDENCIES
    - Install [COMPOSER]
- SETUP INSTRUCTIONS
    - Pull gearman-ui repository
            git clone git://github.com/gaspaio/gearmanui.git gearman-ui
    - Install gearman-ui
            cd gearman-ui
            composer install
    - Enable PHP Module in Apache
            sudo vim /etc/apache2/httpd.conf
        Uncomment this line: `LoadModule php5_module libexec/apache2/libphp5.so`

    - Create Apache virtual host
            <VirtualHost *:80>
                ServerName gearmanui.steponeinc.com
                DocumentRoot "/Users/adampan/Downloads/gearman-ui/web"
                CustomLog /private/var/log/gearman-ui.log combined
                ErrorLog "/private/var/log/gearman-ui.log"

                <Directory />
                    Allow from All
                </Directory>
                <Directory /js>
                    Allow from all
                </Directory>
            </VirtualHost>

        Note the entire `DocumentRoot` path needs to have READ and EXECUTE permission.

    - Restart Apache
            sudo apachectl restart

    - Modify Apache `httpd.conf` to allow rewrite
        
        Find all instances of `AllowOverride` from None to All because gearman-ui uses .htaccess.
    - Copy configuration file
    
            cp app/config/gearmanui.yml.dist app/config/gearmanui.yml
        The yaml file points to localhsot by default.
    - Set default timezone in php.ini
        
        PHP provides a default template located at /etc/php.ini.default and is read-only by default.
        - Copy template as php.ini
                sudo cp /etc/php.ini default /etc/php.ini
        - Set write access
                sudo chmod a+w /etc/php.ini
        - Set default timezone
                vim /etc/php.ini.default
                search for 'timezone'
                uncomment that line and set it to "UTC"
        - Remove write access
                sudo chmod a-w /etc/php.ini
        - Restart Apache
                sudo apachectl restart

[COMPOSER]:https://getcomposer.org/download/
[GEARMAN UI]:https://github.com/gaspaio/gearmanui
[SUPERVISORD]:http://supervisord.org/
[GEARMAN SERVER]:http://ctshryock.com/posts/2011/02/16/setting-up-gearmand.html
