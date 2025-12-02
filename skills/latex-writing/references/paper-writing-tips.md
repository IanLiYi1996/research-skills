# 论文写作技巧速查表

基于 [Paper-Writing-Tips](https://github.com/MLNLP-World/Paper_Writing_Tips) 整理的学术论文写作规范。

---

## Reviewer 视角自查

**以 reviewer 的视角来审视你的论文：**

### 五个核心问题

1. **10分钟内能否抓到重点，理清逻辑？**
   - 忙碌的 reviewer 能否快速理解？
   - 逻辑链条是否清晰？

2. **Motivation 和 Contribution 之间的逻辑是否成立？**
   - 问题是否自然引出解决方案？
   - 因果链是否完整？

3. **三句话内能否说清楚最重要的亮点（贡献）？**
   - 核心创新是什么？
   - 为什么重要？

4. **实验是否验证了 motivation 的合理性？**
   - 每个实验是否有明确目的？
   - 声明是否有证据支撑？

5. **Abstract → Introduction → Method → Experiments 逻辑是否一致？**
   - 各部分之间无矛盾
   - 故事线贯穿始终

---

## 写作技巧

### 呈现优先级

**图 > 表 > Algorithm > 公式 > 文字**

- 一图胜千言
- 用最直观的方式呈现
- 复杂概念优先考虑可视化

### 关键原则

1. **实验篇幅尽量多** - 甚至可占一半篇幅
2. **图、caption 要有相对独立性** - 不看正文也能理解
3. **语言以简明易懂为优** - 清晰优先于复杂
4. **引言、case study 中直观的例子具有重要作用** - 具体例子帮助理解
5. **讲好故事** - 从问题到方案的逻辑流畅

---

## 论文结构

**标准结构：** 摘要 → 引言 → (相关工作/Preliminary) → 方法 → 实验 → 结论

### 摘要 (Abstract)

**核心要素：**
- 前人工作的问题 / Motivation（讲故事）
- 提出的解决方法（可以解释为什么能 work）
- 实验分析部分（关键数字）

### 引言 (Introduction)

**详细结构：**

1. **研究问题的价值** - 为什么这个问题重要
2. **前人的主流做法（及缺陷）** - 肯定前人同时指出问题
3. **借鉴的地方，motivation（出处）** - 灵感来源
4. **提出的方法（粗粒度）** - 高层描述
5. **引言中的举例说明** - 具体例子非常重要！
6. **细粒度解释方法** - 更详细的描述
7. **贡献列表** - 更主流的写法是列举贡献

---

## 各章节写作要点

### Related Work (相关工作)

**核心目标：**
- 展示你对领域的理解
- 明确你的工作与前人的区别
- 承认构建基础，指出差距

**组织策略：**

| 策略 | 适用场景 | 结构 |
|------|----------|------|
| 按时间 | 展示领域演进 | 早期 → 近期 → 本文 |
| 按主题 | 涉及多个技术方向 | 分类讨论，最后比较 |
| 按问题 | 技术论文 | 按解决的挑战分组 |

**批判性分析框架：**

```text
# 弱 - 仅总结
Smith et al. (2022) 提出了一个transformer模型。

# 强 - 批判性定位
Smith et al. (2022) 证明了transformer的优势。
然而，他们需要大量标注数据。我们通过...解决这一局限。
```

**常见错误：**
- 流水账式罗列 → 应按主题分组
- 只说好话 → 需指出局限
- 遗漏近期工作 → 检查近6个月arXiv

**篇幅：** 会议论文15-25篇，重点分析3-5篇

---

### Methods (方法)

**标准结构：**
1. 问题形式化
2. 方法概述（配架构图）
3. 各组件详细描述
4. 训练/优化细节

**核心方法 vs 实现细节：**

| 放在正文 | 放在附录 |
|----------|----------|
| 关键算法创新 | 硬件配置 |
| 新架构组件 | 随机种子 |
| 损失函数 | 完整超参数表 |

**经验法则：** 如果改变它不会改变科学贡献，就是实现细节。

**何时使用伪代码：**
- 复杂多步骤流程 ✓
- 新颖算法 ✓
- 标准操作(SGD) ✗
- 2-3句能说清的 ✗

---

### Experiments (实验)

**标准结构：**
1. 实验设置（数据集、基线、指标）
2. 主要结果
3. 分析（消融、案例研究）
4. 讨论（可选）

**实验设计原则 - 每个实验回答一个问题：**

| 问题 | 实验设计 |
|------|----------|
| 有效吗？ | 与基线对比 |
| 为什么有效？ | 消融实验 |
| 什么情况有效？ | 按类别分析 |
| 多稳健？ | 敏感性分析 |

**消融实验设计：**
- 每次只移除一个组件
- 包含基线模型（移除所有组件）
- 按影响程度排序

**统计显著性：**
- 小改进 (<2%) 必须报告检验
- 至少跑3-5次取均值和标准差
- 报告格式：89.3 ± 0.4%

**处理负面结果：**

```text
# 好 - 诚实且建设性
虽然我们在小数据集上表现略低，但在大规模数据上
展现显著优势，说明方法在数据充足时效果更佳。

# 避免
我们的方法在Dataset-C上不好用。
```

---

### Conclusion (结论)

**结构：**
1. 总结做了什么 (2-3句)
2. 关键发现 (2-3句)
3. 意义/影响 (1-2句)
4. 局限性 (1-2句)
5. 未来工作 (2-3句)

**回扣开头：**

```text
# 引言声明
"当前方法因O(n²)复杂度难以处理长序列。"

# 结论回应
"我们提出的方法将复杂度从O(n²)降至O(n log n)，
实验证实可处理比现有方法长10倍的序列。"
```

**建设性表述局限：**

| 局限 | 建设性表述 |
|------|-----------|
| 计算成本高 | "准确性和效率间的权衡" |
| 需要标注数据 | "半监督扩展可减少依赖" |

**不要包含：**
- 新结果、新方法
- 重复摘要原文
- 过度道歉、过度宣传

**篇幅：** 会议论文半栏到一栏

---

## 公式符号规范

### 基本符号约定

| 类型 | 规范 | 示例 |
|------|------|------|
| 标量 | 小写斜体拉丁字母 | $x$, $y$, $\ell$ (用 `\ell` 代替 `l`) |
| 向量 | 小写加粗 | `\mathbf{x}` 或 `\boldsymbol{\theta}` |
| 矩阵 | 大写加粗 | `\mathbf{A}`, `\mathbf{W}` |
| 有结构的值 | `\boldsymbol` | `\boldsymbol{s}` (句子序列、树、图) |
| 集合 | `\mathcal` | `\mathcal{D}`, `\mathcal{X}` |
| 数域/期望 | `\mathbb` | `\mathbb{R}`, `\mathbb{E}`, `\mathbb{N}` |

### 多字母变量名

公式中超过一个字母的变量或符号，使用正文字体：

```latex
% 正确
\textrm{softmax}(x), \textrm{proj}(v), \textrm{enc}(x)

% 错误 - 斜体会让每个字母看起来像独立变量
softmax(x), proj(v)
```

### 使用预定义函数命令

```latex
% 使用内置命令
\arg\max_{x}, \sin(x), \cos(x), \tanh(x), \exp(x), \log(x)
\inf, \sup, \det, \lim_{x \to \infty}

% 自定义算子
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\ReLU}{ReLU}
```

### 括号匹配

使用 `\left` 和 `\right` 自动匹配括号大小：

```latex
% 正确 - 括号随内容缩放
\left( \sum_{i=0}^{N-1} \alpha_i \mathbf{h}_i \right)

% 错误 - 括号大小不匹配
( \sum_{i=0}^{N-1} \alpha_i \mathbf{h}_i )

% 条件集合
\left\{ x \middle| x \neq \frac{1}{2} \right\}
```

### 多行公式对齐

使用 `align` 环境，等号对齐：

```latex
% 推荐 - 等号对齐
\begin{align}
    E &= mc^2 \\
    C &= B \log_2\left(1+\frac{S}{N}\right)
\end{align}

% 不推荐 - 无对齐
\begin{gather}
    E = mc^2 \\
    C = B \log_2\left(1+\frac{S}{N}\right)
\end{gather}
```

### 公式编号

只对需要引用的公式编号：

```latex
\begin{align}
    E &= mc^2 \nonumber \\        % 不编号
    F &= ma \label{eq:force}      % 编号，用于引用
\end{align}
```

---

## 不间断空格 (~)

使用 `~` 表示不间断空格，防止意外换行：

```latex
Figure~\ref{fig:model}
Table~\ref{tab:results}
Section~\ref{sec:intro}
Equation~\eqref{eq:loss}
BERT~\cite{devlin2019bert}
```

---

## 英文引号

使用 `` ` `` 和 `'` 组合：

```latex
% 正确
``quoted text''
`single quotes'

% 错误 - 不要使用
"quoted text"   % 直引号
"中文引号"       % 中文引号
```

**注意**: 引号只表示"所谓"，不表示直接引用。引用的表述考虑用斜体 `\textit{}`。

---

## 引用命令

### 基本用法

| 命令 | 用途 | 输出示例 |
|------|------|----------|
| `\cite{key}` | 句外引用 | [1] 或 (Author, 2020) |
| `\citet{key}` | 句内引用 (作主语/宾语) | Author et al. (2020) |
| `\citep{key}` | 括号内引用 | (Author et al., 2020) |

### 使用场景

```latex
% 作为句子成分 - 用 \citet
\citet{bert} propose a pre-trained model.

% 不作为句子成分 - 用 \citep 或 \cite
Pre-trained models have shown great success~\citep{bert,gpt2}.
```

### 不同模板的命令

| 模板 | 句内引用 | 句外引用 |
|------|----------|----------|
| ACL/NAACL/EMNLP | `\citet{}` | `\citep{}` |
| COLING | `\newcite{}` | `\cite{}` |
| AAAI/IJCAI | `\citeauthor{} \shortcite{}` | `\cite{}` |
| IEEE | `\citeauthor{}~(\citeyear{})` | `\cite{}` |

---

## 三线表 (Booktabs)

### 基本格式

```latex
\usepackage{booktabs}

\begin{table}[htbp]
    \centering
    \caption{实验结果}
    \label{tab:results}
    \begin{tabular}{lcc}
        \toprule
        Method & Accuracy & F1 \\
        \midrule
        Baseline & 85.2 & 84.1 \\
        Our Model & \textbf{89.3} & \textbf{88.7} \\
        \bottomrule
    \end{tabular}
\end{table}
```

### 重要原则

- **不要画竖线** - 三线表只有横线
- 使用 `\toprule`, `\midrule`, `\bottomrule`
- 多列表头用 `\cmidrule(lr){2-4}` 分隔

### 表格大小调整

```latex
% 字号调整
{\small
\begin{tabular}{...}
...
\end{tabular}
}

% 列间距调整
\setlength{\tabcolsep}{8pt}

% 固定列宽
\begin{tabular}{p{2cm}cc}
```

---

## 图片规范

### 矢量图优先

```latex
% 推荐 - 矢量图
\includegraphics[width=0.8\textwidth]{figure.pdf}

% 不推荐 - 位图 (除非是照片)
\includegraphics[width=0.8\textwidth]{figure.png}
```

### 图片要求

1. **字体大小**: 介于正文字体与 caption 之间，保持一致
2. **颜色**: 不超过 6 种，避免过亮颜色
3. **黑白友好**: 不要仅用颜色区分，使用实线/虚线、不同标记
4. **简洁**: 尽量少用文字描述，同功能模块用统一格式
5. **箭头方向**: 趋于同一方向，避免来回折转

### 子图引用

```latex
% 引用子图
Figure~\ref{fig:model}(a) shows...
```

---

## 写作风格

### 避免缩写

```latex
% 正确
do not, it is, we have, cannot

% 错误
don't, it's, we've, can't
```

### 所有格转换

```latex
% 推荐
the performance of the method
the structure of the model

% 避免
method's performance
model's structure
```

### 拉丁惯用语

| 表达 | 含义 | 用法 |
|------|------|------|
| `e.g.,` | for example | 举例 (逗号不可省) |
| `i.e.,` | that is | 即，换言之 |
| `et al.` | and others | 多作者引用 |
| `etc.` | and others | 列举事物 (不用于人) |

**注意**: `et al.` 或 `etc.` 在句末时，不需要额外句号。

### 避免绝对化表述

| 避免 | 替换为 |
|------|--------|
| obvious | straightforward |
| always | generally, usually, often |
| never | rare, seldom |
| avoid, eliminate | alleviate, relieve |
| better (模糊) | 具体说明哪里更好 |

### 冠词用法

```latex
% a/an 跟着发音走
an LSTM cell    % L 发音 /el/
an F1 score     % F 发音 /ef/
a URL           % U 发音 /ju:/
a unified model

% the 的使用
% 单数可数名词不能单独出现，要么 the 特指，要么复数泛指
the proposed method (特指)
neural networks (泛指)
```

---

## 段落布局

### 最后一行长度

- 最后一行不足 1/4 行宽时，考虑删减或扩充
- 可尝试在段落最后添加 `\looseness=-1`

### Caption 与正文

- **Caption**: 写"这个表格/图是什么"
- **正文**: 写"这个表格/图说明了什么"
- 不要在正文中复述 Caption 内容

---

## 投稿前检查清单

### 内容检查
- [ ] 标题和摘要与投稿系统一致
- [ ] 匿名性 - 无个人/机构信息
- [ ] 代码路径无个人信息
- [ ] 隐藏文件夹 (.git) 已处理

### 格式检查
- [ ] 不超页
- [ ] 所有图表有 \label 和引用
- [ ] 引用格式统一 (会议名缩写一致)
- [ ] 优先引用正式发表版本而非 arXiv

### LaTeX 检查
- [ ] 不间断空格 (~) 使用正确
- [ ] 英文引号格式正确
- [ ] 无编译警告
- [ ] 使用 `\usepackage[english]{babel}` 优化换行

### 图表检查
- [ ] 图片为矢量图
- [ ] 图内字体大小一致
- [ ] 图片两侧无多余空白
- [ ] 颜色不超过 6 种

---

## 参考工具

- [Grammarly](https://app.grammarly.com) - 语法检查
- [Writefull](https://www.writefull.com/) - 学术写作检查
- [SimBiber](https://github.com/MLNLP-World/SimBiber) - BibTeX 简化
- [Rebiber](https://github.com/yuchenlin/rebiber) - BibTeX 规范化
- [aclpubcheck](https://github.com/acl-org/aclpubcheck) - ACL 论文检查

---

## 外部资源

- [清华大学刘洋: 机器翻译学术论文写作方法和技巧](http://nlp.csai.tsinghua.edu.cn/~ly/talks/cwmt14_tut.pdf)
- [复旦大学邱锡鹏: 如何端到端地写科研论文](https://xpqiu.github.io/slides/20181019-PaperWriting.pdf)
- [CMU Graham Neubig: How to Write a Paper](http://www.phontron.com/slides/neubig15paperwriting.pdf)
- [Deep Learning Book Notation](https://www.deeplearningbook.org/contents/notation.html)
