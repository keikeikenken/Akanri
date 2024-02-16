# Akanri
### 解決すべき課題
物理的な制限: タイムカードは物理的な場所が必要であり、リモートワークや外出中の勤務時間の記録が困難。  
データの手動処理: タイムカードのデータをエクセルなどに転記する際の手間とミス。  
不正確な記録: タイムカードの紛失や破損、不正確な打刻による勤怠データの誤り。  
リモートワーク未対応: 在宅勤務者の勤務時間管理の手段が不足。また、現在の勤務状況を把握するのが困難。  
操作性：直感的にあらゆる年齢層が扱えるか  

### KPI 
不正確な記録を０に。  
出退勤記録の管理にかかる時間を半分未満に。  
アプリの使いやすさに関する従業員の満足度を80%以上に。  

### ターゲット
従業員の勤務状況を把握し、出退勤管理を効率化したい企業の管理者。  
自身の勤務時間を正確に記録し、給与計算の正確性を確保したい従業員。  

### ユーザーストーリー
管理者：従業員の出退勤時間をリアルタイムで確認でき、勤務時間が一目で分かる。  
従業員：出勤時と退勤時に簡単な操作で時間を記録でき、自身の勤務記録を過去にさかのぼって確認できる。  

### 仕様詳細
ボタンによる簡単な操作性。  
個々の従業員の勤務時間記録。  
ユーザーフレンドリーなWebインターフェース。  

### 管理者用ダッシュボード？（Redash?勤務時間、遅刻、欠勤の集計と報告）

#### 分析ログ設計
id：勤怠情報の管理ID  
user_id：ログイン情報で管理しているユーザーID  
attendance_time：出勤時間  
leave_time：退勤時間  
working_hours：就業時間  
overtime_hours：残業時間  
break_time：休憩時間  
attendance:出勤したかどうか(1or0)  


