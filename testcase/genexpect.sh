#!/bin/bash
# backup file
mv main/bkit/utils/AST.py main/bkit/utils/AST_Backup.py
mv main/bkit/checker/StaticError.py main/bkit/checker/StaticError_Backup.py
mv test/TestUtils.py test/TestUtils_Backup.py
# move test files to code
mv testfiles/AST.py main/bkit/utils/
mv testfiles/StaticError.py main/bkit/checker/
mv testfiles/TestUtils.py test/
# gen
python3 run.py test CheckSuite 
# move test files out code
mv main/bkit/utils/AST.py testfiles/ 
mv main/bkit/checker/StaticError.py testfiles/
mv test/TestUtils.py testfiles/
# rename file backup
mv main/bkit/utils/AST_Backup.py main/bkit/utils/AST.py
mv main/bkit/checker/StaticError_Backup.py main/bkit/checker/StaticError.py
mv test/TestUtils_Backup.py test/TestUtils.py