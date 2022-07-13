%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Twenty Seconds Curriculum Vitae in LaTex
% ****************************************
%
% License: MIT
%
% For further information please visit:
% https://github.com/spagnuolocarmine/TwentySecondsCurriculumVitae-LaTex
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%
% CLASS %
%%%%%%%%%
\ProvidesClass{twentysecondcv}[2022/11/07 CV class]
\LoadClass{article}
\NeedsTeXFormat{LaTeX2e}

%%%%%%%%%%%%
% PACKAGES %
%%%%%%%%%%%%
\RequirePackage[quiet]{fontspec}
\RequirePackage[sfdefault]{ClearSans}
%\RequirePackage[T1]{fontenc}
\RequirePackage{tikz}
\RequirePackage{xcolor}
\RequirePackage[absolute,overlay]{textpos}
\RequirePackage{ragged2e}
\RequirePackage{etoolbox}
\RequirePackage{ifmtarg}
\RequirePackage{ifthen}
\RequirePackage{pgffor}
\RequirePackage{marvosym}
\RequirePackage{parskip}
\RequirePackage{wrapfig}
\RequirePackage{enumitem}
\RequirePackage{booktabs}
\RequirePackage{fontawesome}
\usepackage{changepage}
\usepackage{smartdiagram}

\setlist[itemize]{leftmargin=*}
\RequirePackage[hidelinks]{hyperref}
\hypersetup{
    pdftitle={},
    pdfauthor={},
    pdfsubject={},
    pdfkeywords={},
    colorlinks=false,           % no lik border color
    allbordercolors=white       % white border twentysecondcvcolor for all
}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
%%%%%%%%%%%
% OPTIONS %
%%%%%%%%%%%
% icons
\newbool{icon}
\DeclareOption{icon}{%
  \booltrue{icon}
}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{
  \PassOptionsToClass{\CurrentOption}{article}
}
\ProcessOptions\relax
\ifbool{icon}{\RequirePackage{fontawesome}}{}

\usetikzlibrary{calc}

\ifxetex
  \usepackage{letltxmacro}
  \setlength{\XeTeXLinkMargin}{1pt}
  \LetLtxMacro\SavedIncludeGraphics\includegraphics
  \def\includegraphics#1#{% #1 catches optional stuff (star/opt. arg.)
    \IncludeGraphicsAux{#1}%
  }%
  \newcommand*{\IncludeGraphicsAux}[2]{%
    \XeTeXLinkBox{%
      \SavedIncludeGraphics#1{#2}%
    }%
  }%
\fi

%%%%%%%%%%
% colors %
%%%%%%%%%%
\definecolor{white}{RGB}{255,255,255}
\definecolor{darkgray}{HTML}{333333}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{sidecolor}{HTML}{E7E7E7}
\definecolor{lightgray}{HTML}{999999}
\definecolor{green}{HTML}{C2E15F}
\definecolor{orange}{HTML}{FDA333}
\definecolor{purple}{HTML}{D3A4F9}
\definecolor{red}{HTML}{FB0B00}
\definecolor{blue}{HTML}{6CE0F1}
\definecolor{pblue}{HTML}{004D70}
\definecolor{mainblue}{HTML}{0395DE}
\definecolor{cerulean}{HTML}{007BA7}
\definecolor{maingray}{HTML}{B9B9B9}
\definecolor{oddsection}{HTML}{0E5484}
\definecolor{evensection}{HTML}{0E5484}
\definecolor{maindarkgray}{HTML}{B3B3B3}
\definecolor{materialpurple}{HTML}{9C27B0}
\definecolor{materialindigo}{HTML}{3F51B5}
\definecolor{materialblue}{HTML}{2196F3}
\definecolor{materialcyan}{HTML}{00BCD4}
\definecolor{materialteal}{HTML}{009688}
\definecolor{materialgreen}{HTML}{4CAF50}
\definecolor{materiallime}{HTML}{CDDC39}
\definecolor{materialamber}{HTML}{FFC107}
\definecolor{materialbrown}{HTML}{795548}
\definecolor{materialred}{HTML}{FF4436}
\definecolor{materialorange}{HTML}{FF5722}




\ifdefined\@cv@print
  \colorlet{green}{gray}
  \colorlet{orange}{gray}
  \colorlet{purple}{gray}
  \colorlet{red}{gray}
  \colorlet{blue}{gray}
  \colorlet{fillheader}{white}
  \colorlet{asidecolor}{sidecolor}
  \colorlet{header}{gray}
\else
  \colorlet{fillheader}{gray}
  \colorlet{header}{white}
  \colorlet{asidecolor}{sidecolor}
\fi

\colorlet{textcolor}{gray}
\colorlet{headercolor}{gray}


%----------------------------------------------------------------------------------------
%	 MISC CONFIGURATIONS
%----------------------------------------------------------------------------------------

% \renewcommand{\bfseries}{\color{black}} % Make \textbf produce coloured text instead

\pagestyle{empty} % Disable headers and footers

\setlength{\parindent}{0pt} % Disable paragraph indentation

% --------------------------------------------------------------------------------------
% 	FONTS
%-------------------------------------------------------------------------------------
\newfontfamily\headingfont[Path = ./fonts/]{segoeuib.ttf}



%%%%%%%%%%%%%%%%%%%%%%%%
% Profile Right SideBar %
%%%%%%%%%%%%%%%%%%%%%%%%

\setlength{\TPHorizModule}{1cm} % Left margin
\setlength{\TPVertModule}{1cm} % Top margin

% compute size of profile picture
\newcommand{\imsize}{\linewidth}
\newlength\imagewidth
\newlength\imagescale
\renewcommand{\imsize}{0.618\linewidth}
\pgfmathsetlength{\imagewidth}{5cm}
\pgfmathsetlength{\imagescale}{\imagewidth/600}

%\newcommand{\profilesection}[2]{{\noindent\color{black!80} \huge #1 \rule[0.15\baselineskip]{#2}{1pt} \vspace{1pt}}}
\newcommand{\profilesection}[2]{\vspace{0pt}{\color{black!80} \huge #1 \rule[0.15\baselineskip]{#2}{1pt} }}

\newcommand{\cvdate}[1]{\renewcommand{\givencvdate}{#1}}                % date
\newcommand{\cvmail}[1]{\renewcommand{\givencvmail}{#1}}                % mail
\newcommand{\cvnumberphone}[1]{\renewcommand{\givennumberphone}{#1}}    % phone
\newcommand{\cvlinkedin}[1]{\renewcommand{\givenlinkedin}{#1}}
\newcommand{\cvtelergram}[1]{\renewcommand{\giventelergram}{#1}}
\newcommand{\cvaddress}[1]{\renewcommand{\givencvaddress}{#1}}          % address
\newcommand{\cvsite}[1]{\renewcommand{\givencvsite}{#1}}                % site
\newcommand{\aboutme}[1]{\renewcommand{\givenaboutme}{  \justifying#1}} % about me
\newcommand{\profilepic}[1]{\renewcommand{\givenprofilepic}{#1}}        % picture
\newcommand{\cvname}[1]{\renewcommand{\givencvname}{#1}}                % name
\newcommand{\cvjobtitle}[1]{\renewcommand{\givencvjobtitle}{#1}}        % job title
\newcommand{\cvrelocation}[1]{\renewcommand{\givencvrelocation}{#1}}        %


\newcommand{\givencvname}{REQUIRED!} % name
\newcommand{\givencvdate}{}          % date
\newcommand{\givencvmail}{}          % mail
\newcommand{\givennumberphone}{}     % phone
\newcommand{\giventelergram}{}
\newcommand{\givenlinkedin}{}
\newcommand{\givencvaddress}{}       % address
\newcommand{\givenaboutme}{}         % about me
\newcommand{\givenprofilepic}{}      % picture
\newcommand{\givencvsite}{}          % site
\newcommand{\givencvjobtitle}{}      % job title
\newcommand{\givencvrelocation}{}

% Command for printing the contact information icons
\newcommand*\icon[1]{\tikz[baseline=(char.base)]{
    \node[shape=circle,draw,inner sep=1pt,
        fill=mainblue,mainblue,text=white,
        minimum size=6mm, maximum size=7mm] (char) {#1};}}

%\newcommand*\icon[1]{\tikz[baseline=(char.base)]{
%\includegraphics[scale=0.05]{img/telegram}
%%  \node[shape=circle,draw,inner sep=1pt, fill=mainblue,mainblue,text=white] (char) {#1};
%}
%}

% Text in square node with rounded corners; #1 -> text, #2 -> color
%\newcommand*\round[2]{%
%\tikz[baseline=(char.base)]\node[anchor=north west, draw,rectangle,
%  rounded corners, inner sep=1.6pt, minimum size=5.5mm, text height=3.6mm,
%  fill=#2,#2,text=white](char){#1};%
%}

% skill bar graphs
\newcommand\skills[3]{
  \renewcommand{\givenskill}{
    \noindent
        ~
        \smartdiagram[bubble diagram]{#1}
        \smartdiagramset{ bubble center node color = materialred }
        \\
        ~
        \smartdiagram[bubble diagram]{#2}
        \smartdiagramset{bubble center node color = green}
        \\
        ~
        \smartdiagram[bubble diagram]{#3}
  }
}

%----------------------------------------------------------------------------------------
%  SIDEBAR LAYOUT
%----------------------------------------------------------------------------------------


\newcommand{\makesidebar}{
  \begin{tikzpicture}[remember picture,overlay]
      \node [rectangle, fill=sidecolor, anchor=north, minimum width=9cm, minimum height=\paperheight+1cm] (box) at (18cm,0.5cm){};
  \end{tikzpicture}

  \begin{textblock}{6}(15, 0.2)
        \profilesection{Soft Skills}{4cm}
        {\begin{itemize}
             \item Responsive
             \item Empathy
             \item Stress Resistance
             \item Meticulous
             \item Self-sufficiency
         \end{itemize}}
  \end{textblock}
}
% text style skills
\newcommand{\givenskill}{}
  \newcommand\skillstext[1]{
    \renewcommand{\giventextskill}{
    \begin{flushleft}
    \noindent
    \foreach [count=\i] \x/\y in {#1}
    {
      \x$ \star $\y
    }
    \end{flushleft}
  }
}

\newcommand{\giventextskill}{}

\newcommand{\makeprofile}
{
  % grey bar on the left side
  \begin{tikzpicture}[remember picture,overlay]
      \node [rectangle, fill=asidecolor, anchor=north, minimum width=9.90cm, minimum height=\paperheight+3cm] (box) at (18cm,2cm){};
  \end{tikzpicture}
 %------------------------------------------------
  \begin{textblock}{6}(14.4, 0.2)
    \begin{flushleft}
%      \hspace{13pt}

      % profile picture
%      \ifthenelse{\equal{\givenprofilepic}{}}{}{\begin{tikzpicture}[x=\imagescale,y=-\imagescale]
%          \clip (600/2, 567/2) circle (567/2);
%          \node[anchor=north west, inner sep=0pt, outer sep=0pt] at (0,0) {\includegraphics[width=\imagewidth]{\givenprofilepic}};
%      \end{tikzpicture}}

      % name
      \vspace{4mm}
      {\Huge\color{pblue}\givencvname}
      %------------------------------------------------
      % jobtitle
%      \begin{flushright}
%        {\Large\color{black!80}\givencvjobtitle}
%      \end{flushright}
      %------------------------------------------------

%        \vspace{5mm}
      \renewcommand{\arraystretch}{1.6}

      \begin{tabular}{ p{1cm}   p{5cm}}
        % CV date
        \ifthenelse{\equal{\givencvdate}{}}{}{\textsc{\icon{\faInfo}} & \givencvdate\\}
        % CV Linkedin
        \ifthenelse{\equal{\givenlinkedin}{}}{}{\textsc{\icon{\faLinkedin}}
          & \href{https://\givenlinkedin}{\givenlinkedin}\\}
        % CV Telegram
        \ifthenelse{\equal{\giventelergram}{}}{}{\textsc{\icon{\faPaperPlane}}
          & \href{https://\giventelergram}{\giventelergram}\\}
        % CV phone
        \ifthenelse{\equal{\givennumberphone}{}}{}{\textsc{\icon{\LARGE\faMobile}}
          & \href{tel:\givennumberphone}{\givennumberphone}\\}
        % CV site
        \ifthenelse{\equal{\givencvsite}{}}{}{\textsc{\icon{\Mundus}}
          & \href{\givencvsite}{\textcolor{cerulean}\givencvsite}\\}
        % CV mail
        \ifthenelse{\equal{\givencvmail}{}}{}{\textsc{\icon{\large\faAt}}
          & \href{mailto:\givencvmail}{\givencvmail}\\}
        % CV address
        \ifthenelse{\equal{\givencvaddress}{}}{}{\textsc{\Large\icon{\faMapMarker}}
          & \href{https://www.google.com/maps/place/Bar,+Montenegro/@42.1021263,19.0706027,10z/}{\givencvaddress}\\}
        % CV relocation
        \ifthenelse{\equal{\givencvrelocation}{}}{}{\textsc{\icon{\faPlane}}
          & \givencvrelocation\\}
      \end{tabular}
      % skills with scale
      \profilesection{Skills}{5cm}
      \givenskill
      \noindent
      \profilesection{Language}{5cm}
        {\begin{itemize}
             \item English text - \textbf{B2}
             \item English speech - \textbf{A2}
             \item Montenegrin - study
             \item Russian - native
         \end{itemize}}
      \noindent
    \end{flushleft}
  \end{textblock}
  \vspace{-10pt}
}


%----------------------------------------------------------------------------------------
%	 COLOURED SECTION TITLE BOX
%----------------------------------------------------------------------------------------

\newcounter{colorCounter}
% Command to create the rounded boxes around the first three letters of section titles
\newcommand*\round[2]{%
	\tikz[baseline=(char.base)]\node[anchor=north west, draw,rectangle, rounded corners, inner sep=1.6pt, minimum size=5.5mm, text height=3.6mm, fill=#2,#2,text=white](char){#1};%
}

\def\@sectioncolor#1#2#3{%
  {%
		\color{mainblue} #1#2#3%
  }%
  \stepcounter{colorCounter}%
}

\renewcommand{\section}[1]{
  \par\vspace{\parskip}
  {%
    \LARGE\headingfont\color{headercolor}%
    \@sectioncolor #1%
  }
  \par\vspace{\parskip}
}

\newcommand{\sectionicon}[2]{
  \par%
  {%
    \LARGE\headingfont
    #1
    \color{headercolor}%
    \@sectioncolor #2%
  }
  \par\vspace{\parskip}
}

\renewcommand{\subsection}[1]{
	\par\vspace{.5\parskip}{%
        \Large\headingfont\color{headercolor} #1%
    }
    \par\vspace{.25\parskip}%
}

\pagestyle{empty}

%----------------------------------------------------------------------------------------
%	 LONG LIST ENVIRONMENT
%----------------------------------------------------------------------------------------

\setlength{\tabcolsep}{0pt}

% New environment for the long list
\newenvironment{twenty}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
%\renewcommand{\bfseries}{\color{headercolor}}
\newcommand{\twentyitem}[5]{%
	\parbox[t]{0.17\textwidth}{#1} &\parbox[t]{0.83\textwidth}{%
    \textbf{#2}%
    \hfill%
    {\footnotesize#3}\\%
    \ifblank{#4}{}{#4 \\}
    #5\vspace{2\parsep}%
  }\\
}
\setlength{\tabcolsep}{0pt}
\newenvironment{twentyicon}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
%\renewcommand{\bfseries}{\color{headercolor}}
\newcommand{\twentyitemicon}[5]{%
 \hspace{3pt}\faicon{#1}\hspace{2pt}#2&\parbox[t]{11.2cm}{%
    \textbf{#3}%
    \hfill%
    {\footnotesize#4}\\%
    #5\vspace{\parsep}%
  }\\%
}

%----------------------------------------------------------------------------------------
%	 SMALL LIST ENVIRONMENT
%----------------------------------------------------------------------------------------

\setlength{\tabcolsep}{0pt}

% New environment for the small list
\newenvironment{twentyshort}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
%\renewcommand{\bfseries}{\color{headercolor}}

\newcommand{\twentyitemshort}[2]{%
  \hspace{5pt}#1&\parbox[t]{11.5cm}{%
    \textbf{#2}%
  }\\%
}
\setlength{\tabcolsep}{0pt}
\newenvironment{twentyshorticon}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
%\renewcommand{\bfseries}{\color{headercolor}}
\newcommand{\twentyitemshorticon}[3]{%
  \hspace{3pt}\faicon{#1}\hspace{3pt}#2&
      \parbox[t]{11.5cm}{%
    \textbf{#3}%
  }\\%
}

%----------------------------------------------------------------------------------------
%	 MARGINS AND LINKS
%----------------------------------------------------------------------------------------

\RequirePackage[left=1cm,top=0.6cm,right=7.2cm,bottom=1cm,nohead,nofoot]{geometry}

\smartdiagramset{
    bubble center node font = \footnotesize,
    bubble node font = \footnotesize,
    % specifies the minimum size of the bubble center node
    bubble center node size = 0.5cm,
    %  specifies the minimum size of the bubbles
    bubble node size = 0.5cm,
    % specifies which is the distance among the bubble center node and the other bubbles
    distance center/other bubbles = 0.5cm,
    % sets the distance from the text to the border of the bubble center node
    distance text center bubble = 0.5cm,
    % set center bubble color
    bubble center node color = mainblue,
    % define the list of colors usable in the diagram
    set color list = {lightgray, materialcyan, orange, green, materialorange, materialteal, materialamber, materialindigo, materialgreen, materiallime},
    % sets the opacity at which the bubbles are shown
    bubble fill opacity = 0.6,
    % sets the opacity at which the bubble text is shown
    bubble text opacity = 1,
}

