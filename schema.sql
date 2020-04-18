create table if not exists readings (time timestamp, ph real, ec real, tds real);
create table if not exists output_schedule (output integer, day integer, time text, command text);
create table if not exists output_mappings (output integer, pin integer, name text);



