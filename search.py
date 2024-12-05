
from typing import Dict, List, Any
import json
from flask import jsonify

class CourseSearch:
    def __init__(self):
        # 初始化變數
        self.timetable_menu_html = {}  # 存放Timetable Menu html
        self.lang_type = 'zh-tw'  # 預設語言為中文
        self.semester_map = {
            'en': {'1':'Fall Semester', '2':'Spring Semester', 'X':'Summer Vacation Semester'},
            'zh': {'1':'上', '2':'下', 'X':'暑'} 
        }
        
    def search_courses(self, params: Dict) -> Dict:
        """執行課程搜尋"""
        try:
            # 檢查搜尋條件
            if not self._validate_search_criteria(params):
                return {'error': '請選擇搜尋條件' if self.lang_type == 'zh-tw' else 'Please choose search criteria'}
                
            # 檢查顯示欄位
            if not self._validate_display_columns(params):
                return {'error': '請至少選擇一個顯示欄位' if self.lang_type == 'zh-tw' else 'Please choose at least one display column'}
            
            # 組合查詢參數
            query_params = self._build_query_params(params)
            
            # 執行搜尋
            results = self._execute_search(query_params)
            
            return {
                'status': 'success',
                'data': results
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    def _validate_search_criteria(self, params: Dict) -> bool:
        """驗證搜尋條件"""
        return any([
            params.get('chk_acysem'),
            params.get('chk_dep'),
            params.get('chk_campus'),
            params.get('chk_option')
        ])

    def _validate_display_columns(self, params: Dict) -> bool:
        """驗證顯示欄位"""
        display_columns = params.get('display_columns', [])
        return len(display_columns) > 0

    def _build_query_params(self, params: Dict) -> Dict:
        """建立查詢參數"""
        query = {
            'm_acy': params.get('acy', '**'),
            'm_sem': params.get('sem', '**'),
            'm_acyend': params.get('acyend', '**'),
            'm_semend': params.get('semend', '**'),
            'm_dep_uid': params.get('dep_uid', '**'),
            'm_option': params.get('option', '**'),
        }
        
        # 處理特殊條件
        if params.get('category') == '0U':
            query['m_option'] = 'approved_General'
            
        return query

    def _execute_search(self, query_params: Dict) -> List:
        """執行資料庫查詢"""
        # 這裡實作實際的資料庫查詢邏輯
        # 需要根據實際的資料庫結構來實作
        pass

    def get_course_list(self, params: Dict) -> Dict:
        """取得課程列表"""
        try:
            results = self.search_courses(params)
            return jsonify(results)
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            })

# 使用範例
if __name__ == '__main__':
    course_search = CourseSearch()
    
    # 測試搜尋參數
    test_params = {
        'acy': '111',
        'sem': '1',
        'dep_uid': 'CS',
        'display_columns': ['cos_id', 'cos_name'],
        'chk_acysem': True,
        'chk_dep': True
    }
    
    # 執行搜尋
    result = course_search.search_courses(test_params)
    print(json.dumps(result, indent=2, ensure_ascii=False))