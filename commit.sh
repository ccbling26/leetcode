#!/bin/bash
read -p "输入上传内容: " number
git add $number
git commit -m "add $number"
git push
