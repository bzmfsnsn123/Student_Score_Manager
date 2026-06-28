FIlE_NAME="score.txt"
def load_score():
    score_dict={}
    try:
        with open(FIlE_NAME,"r",encoding="utf-8") as f:
            for line in f.readlines():
                line=line.strip()
                if not line:
                    continue
                name,score=line.split(",")
                score_dict[name]=int(score)
    except FileNotFoundError:
        pass
    return score_dict
def save_score(data):
    with open(FIlE_NAME,"w",encoding="utf-8") as f:
        for name,score in data.items():
            f.write(f"{name},{score}\n")
def main():
    student_data=load_score()
    while True:
        print("\n=====学生成绩管理系统=====")
        print("1.添加学生成绩")
        print("2.查询单个学生成绩")
        print("3.查看全班成绩&统计")
        print("4.修改学生分数")
        print("5.删除学生记录")
        print("0.退出程序")
        try:
            opt=int(input("请输入功能序号"))

            if opt==1:
                name=input("请输入学生姓名：").strip()
                if name=="":
                   print("姓名不能为空")
                   continue
                if name in student_data:
                    print(f"{name}已存在，不能重复添加！")
                score=int(input("请输入考试成绩："))
                if 0<=score<=100:
                    student_data[name]=score
                    save_score(student_data)
                    print(f"✅{name}成绩添加成功！")
                else:
                    print("分数必须在0-100之间")

            elif opt==2:
                   search_name=input("输入要查询的学生姓名：").strip()
                   if search_name in student_data:
                       print(f"{search_name}的分数:{student_data[search_name]}")
                   else:
                       print("❌该学生不存在")

            elif opt==3:
                if not student_data:
                    print("没有学生数据")
                    continue
                print("\n全班成绩列表：")
                for n,s in student_data.items():
                    print(f"{n}：{s}分")
                scores_list=list(student_data.values())
                avg=sum(scores_list)/len(scores_list)
                max_s=max(scores_list)
                min_s=min(scores_list)
                print(f"\n全班人数：{len(student_data)}")
                print(f"平均数：{avg:1f} 最高分：{max_s} 最低分：{min_s}")

            elif opt==4:
                edit_name=input("输入要修改的学生姓名").strip()
                if edit_name not in student_data:
                    print("学生不存在")
                    continue
                new_score=int(input("输入新分数："))
                if 0<=new_score<=100:
                    student_data[edit_name]=new_score
                    save_score(student_data)
                else:
                    print("分数超过0-100！")

            elif opt==5:
                del_name=input("请输入要删除学生的姓名").strip()
                if del_name in student_data:
                    del student_data[del_name]
                    save_score(student_data)
                    print(f"✅{del_name}已删除！")
                else:
                    print("该学生不存在")

            elif opt==0:
                print("数据已保存，程序退出！")
                break
            else:
                print("请输入0-5的数字")
        except ValueError:
            print("❌输入错误，请输入合法数字")

if __name__=="__main__":
    main()









