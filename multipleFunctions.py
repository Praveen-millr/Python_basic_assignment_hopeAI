class formula():
    def Subfield():
        print("Subfields in AI are:")
        fields = ['Machine learning','Nural network','Computer vison','Robotic','Speech processing','NLP']
        for text in fields:
            print(text)
    
    def Oddeven():
        num=int(input("Enter the num:"))
        if num%2==0:
            print("The number is even")
        else:
            print("The number is odd")

    def MarrageElegibility():
        Gender=input("Enter Gender")
        Age=int(input("Enter the Age:"))
        if Gender == 'male':
            if Age>=21:
                print("Elegible")
            else:
                print("Not elegible")
        
        elif Age>=18:
            print("Elegible")
        else:
            print("Not eligible")   

    def percentages():
        tamil=int(input("Enter tamil mark:"))
        socialScience=int(input("Enter socialScience mark:"))
        english=int(input("Enter english mark:"))
        matchs=int(input("Enter matchs mark:"))
        science=int(input("Enter science mark:"))
        Total = tamil+socialScience+english+matchs+science
        percentage = 100/500*Total
        print("Tamil:",tamil)
        print("socialScience:",socialScience)
        print("English:",english)
        print("matchs:",matchs)
        print("science:",science)
        print("Total:",Total)
        print("percentage:",percentage)

    def triangle():
        triangleHeight = int(input("Enter triangel Height:"))
        triangleBreadth = int(input("Enter triangel Breadth:"))
        print("Area of triangle:",(triangleHeight*triangleBreadth)/2)
        perimeterHeight1 = int(input("Enter perimeter Height1:"))
        perimeterHeight2 = int(input("Enter perimeter Height2:"))
        perimeterBreadth = int(input("Enter perimeter Breadth:"))
        print("Perimeter of triangle:",(perimeterHeight1+perimeterHeight2+perimeterBreadth))