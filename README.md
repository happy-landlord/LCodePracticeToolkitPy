# LeetCode Local Practice with Automation Toolkit in Python3


## Prerequisites
This project only supports Python3 on OS X and is NOT compatible with any other envs.
Also require: 
```bash
pip3 install pyperclip
```

## 工作流

1. 使用 `python3 tool/init.py <problem_number>` 创建问题文件`<problem_number>.py`。
2. 用剪贴版(只支持OS X)中已经写入的prompt，找生成式AI要：题目，模版&测试用例。
3. 把获得的模版&测试用例，粘贴回`<problem_number>.py`。
4. 实现代码后，直接运行 `<problem_number>.py` 文件，即可执行测试用例。

## 可单独使用的命令

### 1. 生成获得LeetCode某问题的prompt

命令：

```bash
python3 tool/prompt.py <problem_number>
```

- `<problem_number>`：（例如 `28`）。
- 功能：写入`tool/prompt_generate_lc_problem.md`的内容到OS X的剪贴板。

### 2. 单独运行某问题的测试用例

命令：

```bash
python3 test/test_runner.py <problem_number>
```

- `<problem_number>`：（例如 `1768`）。
- Output as below (1768 in this case)

```
  🎉🎉🎉🎉🎉 LeetCode 1768 🎉🎉🎉🎉🎉

  Test Case 1: ✅
  Input: word1 = abc, word2 = pqr
  Expected: apbqcr
  Actual  : apbqcr
  
  Test Case 2: ✅
  Input: word1 = ab, word2 = pqrs
  Expected: apbqrs
  Actual  : apbqrs
  
  Test Case 3: ✅
  Input: word1 = abcd, word2 = pq
  Expected: apbqcd
  Actual  : apbqcd
  
  Summary: 3/3 tests passed (100.00%)

```