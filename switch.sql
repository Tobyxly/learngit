update salary 
    set 
        sex = case 
        when 'f' then 'm'
        else 'f'
    end;
