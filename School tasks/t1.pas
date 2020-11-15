var x, m, n: integer;
begin
    readln(x);
    m:=0; n:=0;
    while x>0 do
        begin
            if n<x mod 10 then n:=x mod 10;
            m:=m+1;
            x:=x div 10;
        end;
    writeln(m); write(n)
end.