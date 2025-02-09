git remote add origin https://github.com/raywkhon/python.git
git branch -M main
git push -u origin main 
git pull https://github.com/raywkhon/python.git

git push https://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@github.com/raywkhon/python.git

git remote -v

git remote remove origin

https://github.com/raywkhon/python.git
https://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@github.com/raywkhon/python.git


>> C:/Program Files/Git/bin/git.exe commit -F C:/Users/Raymond/AppData/Local/Temp/RtmpcnsS8m/git-commit-message-1b105d7e6015.txt --amend
[main bbc8a18] Commit python 4
Date: Sat Feb 8 18:47:52 2025 +0000
19 files changed, 664183 insertions(+)
create mode 100644 .gitignore
create mode 100644 NGC_3198_RO_MOM1_THINGS.FITS
create mode 100644 frame-g-007923-5-0307.fits
create mode 100644 gaia-plot.pdf
create mode 100644 gitcommand.R
create mode 100644 histogram.pdf
create mode 100644 hst_05773_05_wfpc2_f502n_wf_drz.fits
create mode 100644 hst_05773_05_wfpc2_f656n_wf_drz.fits
create mode 100644 hst_05773_05_wfpc2_f673n_wf_drz.fits
create mode 100644 pyastro.py
create mode 100644 pyastro2.py
create mode 100644 python.Rproj
create mode 100644 sdss-py.pdf
create mode 100644 spec-1330-52822-0304.fits
create mode 100644 spectrum.fits
create mode 100644 test.R
create mode 100644 zoo2MainSpecz.csv
create mode 100644 zoo2MainSpecz.fits
create mode 100644 zoo2MainSpecz2.csv

git reset 
git rebase -i HEAD~2