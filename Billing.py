import pandas as pd
print("New --To make a new product list")
print("Update --To update product list as a CSV file")
print("Bill --Billing")
choice=str(input("What u wanna do: "))

if choice=="Add":
    print("\n")
    print("CSV --add through CSV_file")
    print("New --add manually (Dictionary): \n")
    choice_2=str(input("By what u wanna add: "))
    
    if choice_2=="New":
        x=[]
        y=[]
        z=[]
        p=[]
        product_dict={"Product_Name":x,"Product_Code":y,"Product_Price":z,"Product_in_stock":p}
        lst_product=list(product_dict.keys())
        data_length=int(input("No. of data to be entered: "))
        for i in range(0,data_length):
            for a in range(0,len(lst_product)):
                str_1="Add in {}: "
                add=str(input(str_1.format(lst_product[a])))
            
                if lst_product[a]=="Product_Name":
                    x.append(add)
                    
                elif lst_product[a]=="Product_Code":
                    y.append(add)
                    
                elif lst_product[a]=="Product_Price":
                    z.append(add)
        
                elif lst_product[a]=="Product_in_stock":
                    p.append(add)
                a+=1
            print("\n")
        #print(x)
        #print(y)
        #print(z)
        #print(p)
        df=pd.DataFrame(product_dict)
        print(df,"\n")
        
        print("If Yes then, save with name (Eg:/home/linux/code/Billing.csv)")
        choice_3=str(input("Wana save the dataframe as a CSV_File (Y/N): "))
        if choice_3=="Y":
            location=str(input("Give a location to save: "))
            sep=str(input("Provide seperator in CSV file"))
            edf=df.to_csv(location,sep)
        else:
            pass
        
    elif choice_2=="CSV":
        print("Not available right now!!")

elif choice=="Update":
    print("Not Available for now")
        
elif choice=="Bill":
    print("Let's start the goddamn business!!")
    location=str(input("Give location of Product_list: "))
    sep=str(input("Give seprator used: "))
    df=pd.read_csv(location,sep)
    
    dict_df=dict(df)
    name=list(dict_df.get("Product_Name"))
    code=list(dict_df.get("Product_Code"))
    price=list(dict_df.get("Product_Price"))
    stock=list(dict_df.get("Product_in_stock"))
    print(code)
    print("\nProduct List")
    print(df)
    print("\n")
    prd_code=""
    x=[]
    while prd_code !="Done":
        prd_code=str(input("Scan the bar code or Feed the code manually from above: "))
        if "Done" not in prd_code:
            for a in range(0,len(code)):
                if prd_code==str(code[a]):
                    x.append(prd_code)
            print(x)
            print("Type Done --if done lsting selling products")
        else:
            #Price list
            p=[]
            print("\nCode         Product         Price")
            for i in range(0,len(x)):
                #Elemnt of list x list
                c=int(x[i])
                #Index at which a particualr element in x list is in present in code list
                y=code.index(c)
                #
                p.append(price[y])
                #
                str_1="{}        {}      {}"
                print(str_1.format(code[y],name[y],price[y]))
                #
                i+=1
            net_amt=sum(p)
            print("NET AMOUNT=",net_amt)
            rec=int(input("Amt Recived: "))
            
            while rec<net_amt:
                print("U need more i.e=",net_amt-rec)
                net_amt=net_amt-rec
                rec=int(input("Enter money recived now="))
            else:
                print("Return=",rec-net_amt)
            print("ThankYou")                
