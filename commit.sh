#!/bin/bash
read -p "输入上传内容: " number
git add $number
git cmm "add $number"
git push
