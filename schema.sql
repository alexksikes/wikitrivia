create table wikitrivia_cache (
    id              int(11) not null auto_increment primary key,
    category        varchar(100),
    answer          varchar(150),
    wiki_url        varchar(250) not null unique,
    image_url       varchar(250),
    snippet         text,
    snippet_secret  text,
    index(wiki_url)    
) type=InnoDB; charset utf8;
