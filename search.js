var Timetable_Menu_Html = new Object; //存放Timetable Menu html
var Acy_Sem;
var Lang_Type;  //zh-tw:中文;en-us:英文
var FType; //項目選項
var Timetable_Choose_Time_Html;
var Timetable_Main_Table_Html = new Object;
var English_Semester = {'1':'&nbsp;Fall Semester','2':'&nbsp;Spring Semester','X':'&nbsp;Summer Vacation Semester'};
var Chinese_Semester = {'1':'上','2':'下','X':'暑'};
var Cos_Data_List;
var Chk_Acysem;
var Chk_Dep;
var Chk_Campus;
var Chk_Option;
var Time_Code;
var Classroom_Code;
var Time_Classroom_Code_Html = new Object;
var Html_Content = []; //紀錄取得的HTML頁面內容

//var Select_Option_Data = {};
//Select_Option_Data['zh-tw'] = {};
//Select_Option_Data['en-us'] = {};

Lang_Type = 'zh-tw'; //預設語言為中文

function click_Search_button(){
    $('#crstime_search').bind('click',function(){
        // 初始化參數
        let searchParams = {
            m_acy: '**',
            m_sem: '**', 
            m_acyend: '**',
            m_semend: '**',
            // ...其他搜尋參數
        };

        // 檢查必填搜尋條件
        let validSearch = checkSearchCriteria(); 
        
        if(validSearch){
            // 檢查顯示欄位
            let validColumns = checkDisplayColumns();
            
            if(validColumns){
                // 執行搜尋
                $('#div_loading').addClass("loading");
                
                $.ajax({
                    type: "POST",
                    url: modulePath + "?r=main/get_cos_list",
                    data: searchParams,
                    success: function(json) {
                        Cos_Data_List = json;
                        // 顯示結果
                        get_view_html_content('timetable_main_table',Lang_Type);
                    }
                });
            } else {
                alert(Lang_Type=='zh-tw' ? 
                      "請至少選擇一個顯示欄位" : 
                      "Please choose at least one display column.");
            }
        } else {
            alert(Lang_Type=='zh-tw' ?
                  "請選擇搜尋條件" :
                  "Please choose search criteria."); 
        }
    });
}

// 新增檢查函數
function checkSearchCriteria() {
    return Chk_Acysem || Chk_Dep || Chk_Campus || Chk_Option;
}

function checkDisplayColumns() {
    return $('#tbl_timetable_menu').find('input[type="checkbox"]:checked').length > 0;
}


