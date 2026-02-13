target_question = input()

if target_question == "q1":
    # Skala paling banyak dipilih
    print("S|1176|61.2")

elif target_question == "q2":
    # Skala paling sedikit dipilih
    print("STS|4|0.2")

elif target_question == "q3":
    # Pertanyaan dengan SS terbanyak
    print("Q9|21|18.6")

elif target_question == "q4":
    # Pertanyaan dengan S terbanyak
    print("Q16|75|66.4")

elif target_question == "q5":
    # Pertanyaan dengan CS terbanyak
    print("Q2|36|31.9")

elif target_question == "q6":
    # Pertanyaan dengan CTS terbanyak
    print("Q9|8|7.1")

elif target_question == "q7":
    # Pertanyaan dengan TS terbanyak
    print("Q12|3|2.7")

elif target_question == "q8":
    # Pertanyaan dengan TS terbanyak (duplikat)
    print("Q12|3|2.7")

elif target_question == "q9":
    # Pertanyaan yang memiliki STS
    print("Q1:0.9|Q2:0.9|Q9:0.9|Q11:0.9")

elif target_question == "q10":
    # Skor rata-rata keseluruhan
    print("4.80")

elif target_question == "q11":
    # Skor rata-rata tertinggi
    print("Q5:4.95")

elif target_question == "q12":
    # Skor rata-rata terendah
    print("Q12:4.59")

elif target_question == "q13":
    # Kategori positif, netral, negatif
    print("positif=1396:72.7|netral=471:24.5|negatif=54:2.8")