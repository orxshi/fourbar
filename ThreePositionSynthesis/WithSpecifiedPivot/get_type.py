def get_type(a, b, c, d):

        sort = sorted([a, b, c, d])

        s = sort[0]
        p = sort[1]
        q = sort[2]
        l = sort[3]

        # determine type
        if (s + l) < (p + q):
                typ = 'grashof'
        elif (s + l) > (p + q):
                typ = 'non-grashof'
        else:
                typ = 'special'

        # determine code
        if typ == 'grashof':
            if s == d:
                    code = 'GCCC'
            elif s == a:
                    code = 'GCRR'
            elif s == b:
                    code = 'GRCR'
            elif s == c:
                    code = 'GRRC'
        elif typ == 'non-grashof':
            if l == d:
                    code = 'RRR1'
            elif l == a:
                    code = 'RRR2'
            elif l == b:
                    code = 'RRR3'
            elif l == c:
                    code = 'RRR4'
        else:
            if s == d:
                    code = 'SCCC'
            elif s == a:
                    code = 'SCRR'
            elif s == b:
                    code = 'SRCR'
            elif s == c:
                    code = 'SRRC'
                                
        return typ, code


#typ, code = get_type(16, 257, 80, 218)
#print(typ, code)
