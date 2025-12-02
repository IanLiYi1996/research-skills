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
