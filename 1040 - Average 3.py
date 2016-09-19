x, y, z, w = map(float,raw_input().split())

med = (x*2+y*3+z*4+w*1)/10
print "Media: %.1f" % med

if med >= 7:
    print "Aluno aprovado."
elif med < 5:
    print "Aluno reprovado."
elif 5 <= med <= 6.9:
    print "Aluno em exame."
    nota_exame = float(input())
    print "Nota do exame: %.1f" % nota_exame
    final = (med + nota_exame)/2
    if final >= 5:
        print "Aluno aprovado."
        print "Media final: %.1f" % final
    elif final < 5:
        print "Aluno reprovado."
        print "Media final: %.1f" % final
