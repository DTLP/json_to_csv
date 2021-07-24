# json_to_csv
Converting JSON files to CSV

## Requirements: ##  
pandas            1.0.5

## How to: ## 
### Simple JSON: ###  
With simple JSON when the whole file consists of one array like the example below, you can use the following command to run the script:
```
py.exe .\json_to_csv.py --in .\file.json --out .\file.csv
```
```
[
   {
      "name":"John",
      "surname":"Doe",
      "age":33,
      "fav_things":{
         "food":"Pizza",
         "number":13,
         "sport":"Football"
      }
   },
   {
      "name":"Jack",
      "surname":"Mc'Donald",
      "age":26,
      "fav_things":{
         "food":"Fish and chips",
         "number":7,
         "sport":[
            "Tennis",
            "Basketball"
         ]
      }
   }
]
```
The output would look like this:
name | sirname | age | fav_things_food | fav_things_number | fav_things_sport 
--- | --- | --- | --- |--- |---
John | Doe | 33 | Pizza | 13 | Football
Jack | Mc'Donald | 26 | Fish and chips | 7 | Tennis, Basketball

### Complex JSON: ### 

With complex JSON structure where you might have other arrays or data you don't want to put in the CSV, you can 
specify the name of the array containing only the data you want by using the `--array` flag. Here is an example:
```
py.exe .\json_to_csv.py --in .\file.json --out .\file.csv --array people
```
```
{
   "date":"21/10/2015",
   "people":[
      {
         "name":"John",
         "surname":"Doe",
         "age":33,
         "fav_things":{
            "food":"Pizza",
            "number":13,
            "sport":"Football"
         }
      },
      {
         "name":"Jack",
         "surname":"Mc'Donald",
         "age":26,
         "fav_things":{
            "food":"Fish and chips",
            "number":7,
            "sport":[
               "Tennis",
               "Basketball"
            ]
         },
         "pets":{
            "dogs":{
               "name":"Chappie"
            },
            "cats":{
               "name":"Marmalade"
            }
         }
      }
   ],
   "api_version":"1.0.15",
   "metadata":[
      {
         "date":"21/10/2015",
         "time":"15:13:11"
      }
   ]
}
```
The output of the JSON above will look like this:
name | sirname | age | fav_things_food | fav_things_number | fav_things_sport | pets_dogs_name | pets_cats_name
--- | --- | --- | --- |--- | --- | --- | ---
John | Doe | 33 | Pizza | 13 | Football | |
Jack | Mc'Donald | 26 | Fish and chips | 7 | Tennis, Basketball | Chappie | Marmalade
