# -*-*-*-*- coding: utf-8 -*-*-*-*-
from aip import AipNlp
import re

""" 你的 APPID AK SK """
APP_ID = '14941681'
API_KEY = 'XnnpRK5zSZF33BRpBKqVZdj3'
SECRET_KEY = 'qTxvGRkZZ6YrY72LzF8KQyqlMiefMNmI'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
title = "国内考级与国外考级的异同"
content = '''<div style="margin-left:0px; margin-right:10px">
<div style="margin-left:0px; margin-right:0px">&nbsp;</div>

<div style="margin-left:0px; margin-right:0px">　　在多年的教学中，我既带学生考过国内的考级，也带学生参加过英国皇家<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">音乐</a>学院的考级。随着对国外考级制度的深入了解我确实感受到国外考级制度的科学性，以及对普及广泛的<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">音乐</a>知识，培养学生懂得欣赏<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">古典音乐</a>而起到的重要作用。</div>

<div style="margin-left:0px; margin-right:0px"><strong>［单一性与复合性的差异］</strong></div>

<div style="margin-left:0px; margin-right:0px">　　从技巧上来说，部分孩子手指头的功夫确实了不得。但我们培养了一大堆的<a href="http://www.chinayinji.com/a/leqi/" style="margin:0px;padding:0px;color:#454545;" target="_blank">钢琴</a>匠！有些孩子以优异的成绩通过了考级，但只要你与他们交谈，就会发现他们在音乐知识方面简直是&ldquo;白丁&rdquo;。不但说不出这首乐曲是什么时期的作品，音乐风格，创作背景，乐曲的结构，对这首作品该如何理解，有些孩子甚至连乐曲的曲名，作者是谁都不知道。而国外（包括香港也使用英皇考级体系）的孩子，因没有家长的督促，学琴只是靠兴趣，所以产生了两极分化的现象。一部分学生的技巧差得没法听，可另一部分学生在演奏起来，你却能感受到他懂音乐，他们用音乐与你交谈。他们酷爱音乐，可以到达人迷的程度。他们的表演极具感染力，对比之下，你会惊讶地发现他们掌握的音乐知识是如此的丰富，而他们也只不过就是业余的学生，却能准确地说出乐曲的创作背景，乐曲结构，是何种风格，及作曲家的生平、趣事，他们的学识和能力呈现出复合性的特色。</div>

<div style="margin-left:0px; margin-right:0px">&nbsp;</div>

<div style="margin-left:0px; margin-right:0px"><strong>［考级系统的差异］</strong></div>

<div style="margin-left:0px; margin-right:0px">　　同样是为了普及古典音乐，促进青少年业余音乐的学习，为何国内的考级与国外的考级在孩子们身上所产生的结果会如此的不同？就这种现象，我也曾与一位香港的同行交流过，他认为，归根结底还是考级的系统不同：在乐曲技巧难度方面（包括基本练习，如音阶、琶音等）国内与国外 ( 英皇 ) 考级的程度差不多，差异就出现在&ldquo;视奏&rdquo;&ldquo;听力测试&rdquo;和&ldquo;乐理笔试&rdquo;这些方面。</div>

<div style="margin-left:0px; margin-right:0px">　　英国皇家<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">音乐学</a>院的考级，较重视对乐曲大量的浏览，以提高视奏的能力，要求孩子随便抽一首同等程度或略低的乐段，能当场以略慢的速度弹奏出来，但不能有错音，不能停顿，节奏、奏法要正确，这就要求孩子有相当高的视奏能力。</div>

<div style="margin-left:0px; margin-right:0px">　　在听力测试方面，英国皇家音乐学院的考级也与同内权威中央音乐学院的音乐基础知识测试不同。中央音乐学院考级的音乐基础知识测试与报考中国或中央专业音乐院校的视唱练耳训练都是一样的，专业性很强。如各级测试题均分为两个部分，第一部分为&ldquo;听觉分析&rdquo; : 从模唱单音、音阶、音级、短旋律到听辨二声部旋律，从听辨音程到和弦及其转位和和弦连接；从听辨简单的节拍与节奏到视谱 &ldquo;读&rdquo;较复杂的节奏。第二部分为视谱即唱：从初级无升降的调逐步唱到七个升降记号的凋，以及三个升降记号内的宫、商、角、徵、羽五声调式，节拍从简单的2/4、3/4、4/4、3/8、6/8一直到复杂的9/8、12/8 拍；节奏从附点音符，切分节奏，跨小节连线到连接切分节奏，三连音等，一系列严格、系统的视唱练耳专业课的训练以逐步掌握视唱练耳的技能。如此的考试，我个人认为这作为专业音乐院校的听力训练课程非常好，但作为一种普及全民<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">音乐教育</a>的手段，这样枯燥的练习，往往会让一般的琴童、中小学生或是喜欢音乐，想学音乐而未必有机会到音乐学院中接受全面的<a href="http://www.chinayinji.com/" style="margin:0px;padding:0px;color:#454545;" target="_blank">音乐教育</a>等这一大部分的人对音乐望而却步，让古典音乐真的变得如古语所云&ldquo;曲高和寡&rdquo;。</div>

<div style="margin-left:0px; margin-right:0px">　　我所看到的英国皇家音乐学院的听力测试则完全不一样。它从学习欣赏古典音乐为出发点，要求学生听大量的唱片，从训练学生分析乐曲的节拍、节奏，强度对比（弱 / 强），音量的对比（渐强 / 渐弱）起。如在英皇四级的考试中考官就会与考生讨论以下乐曲的基本特征：</div>

<div style="margin-left:0px; margin-right:0px">　　1.Contrasted dynamics （强弱对比）。乐曲的强弱对比，最大声在那里？这首乐曲是否全部都是小声，结尾是大声还是小声；</div>

<div style="margin-left:0px; margin-right:0px">　　2.Gradation of tone( 音量变化 ) 。 crescendo( 渐强 ) ， diminuendo （渐弱）， Gradual （逐渐）， Sudden （突然）强或弱；</div>

<div style="margin-left:0px; margin-right:0px">　　3.Articulation （发音法）。整首乐曲是以 legato （圆滑奏）还是以 Staccato （断奏）为主？乐曲里面哪一句才是 staccato 或是 legato ，有时候左手弹旋律理 legato 而右手伴奏是 staccato 或相反，乐曲中间有没有改变过？</div>

<div style="margin-left:0px; margin-right:0px">　　4.Tempo changes( 速度改变 ) 。速度是快板、行板还是中板，中间或结尾有没有速度改变，怎样改变（渐慢 / 渐快）？</div>

<div style="margin-left:0px; margin-right:0px">　　5.（乐曲特征） character of the piece 。是几拍子的乐曲？乐曲的节奏特点是乍样的？大调还是小调？为什么？乐曲中有没有转调，乐曲听起来是快乐、活泼，或者有生气还是温柔、宁静、抒情、悲伤的，请说出整首乐曲的感觉。乐曲是属于何种创作风格或乐曲是哪位作曲家的作品，为什么？你对这位作曲家有什么认识，请谈一谈这首乐曲的曲式、结构、织体请分析一下等。</div>

<div style="margin-left:0px; margin-right:0px">&nbsp;</div>

<div style="margin-left:0px; margin-right:0px"><strong>［物理形态和本体形态角度的差异］</strong></div>

<div style="margin-left:0px; margin-right:0px">　　要想通过这样的讨论，考生平时就需要有意识地查看大量的音乐文献，来了解不同时期作品的风格有什么不同，主要作曲家的生平历史、趣事、佳话，经典作品的创作背景，如何分析乐曲的曲式、结构、织体等等，最重要的还是要听大量的唱片来比较分析，印证理论的学习，化被动的学习为主动的研究，而这是我们国内的学生最缺乏的一点。另外，英国皇家音乐学院的乐理考试，不但专业而且趣味性也十足，包括一些作曲的基本技能，如一些节奏的创作，给一段诗句创作八小节的旋律等，这是对创作能力的培养。而我们的教学体系就不太重视这方面能力的培养。我们以前所学的乐理知识，普遍都过于理论化，从音的物理属性、频率、振幅等开始讲起，接着是泛音列，一直到各种律制的区别。初学音乐者面对这些繁琐的学问常会望而却步，或干脆不学音乐理论，只顾弹琴的技巧。但是，乐谱上的各种术语，标记和符号在不同时代的音乐作品中的实际意义，各种装饰音的演奏方法。音乐的分句却一概不知。而英国皇家音乐学院的乐理书不但解决了上面讲到的那些初学音乐者时常遇到的问题，还有大量实用的音乐知识，如和声与旋律方面的基本概念，各种<a href="http://www.chinayinji.com/a/leqi/" style="margin:0px;padding:0px;color:#454545;" target="_blank">乐器</a>各种乐队合奏以及合唱的介绍，甚至还有中古和现代音乐方面的知识，从本体形态的角度来理解西方音乐的入门学习，让考生从理论上丰富自己音乐方面的知识。</div>

<div style="margin-left:0px; margin-right:0px">　　例，英国皇家音乐学院五级乐理课程范围</div>

<div style="margin-left:0px; margin-right:0px">　　1. 5/4 、 7/4 、 5/8 、 7/8 等不规则拍子记号，和在这些节奏中的音符组合，还有在单拍子中的不规则分拍。</div>

<div style="margin-left:0px; margin-right:0px">　　2. 次中音谱号。在四种谱号及本级课程范围内的各种调号的乐谱中辨认音符，把一段简单旋律在不同谱号之间作八度移调，把一段为降 B 、 A 或 F 调乐器创作的旋律在记谱音高和实际演奏音高之间作改写。把一段为 SATB 混声组合创作的音乐在升列总谱和缩编谱之间改写。</div>

<div style="margin-left:0px; margin-right:0px">　　3. 直至六个升／降号的所有大调和小调，这些调的音阶和调号，在任何音符之间构成的单、复音程。</div>

<div style="margin-left:0px; margin-right:0px">　　4. 在任何一个调之中辨认主、上主、下属、属等四个和弦中的 5/3 和 6/3 组合，在任何一个调之中辨认，在属音上面的 6/4 、 5/3 进行，和在其中的 6/4 和弦，用任何可行的记谱方法，为一段 C 、 G 、 D 或 F 调简单旋律中的终止或选择适当和弦。</div>

<div style="margin-left:0px; margin-right:0px">　　5. 使用一个指定的开端，为一件指定的乐器创作一段不超过八小节简短旋律或 ( 由考生自己决定 ) 为一段指定诗句谱写旋律，在旋律中须加上有关速度、力度、发音法等的适当演奏指示。</div>

<div style="margin-left:0px; margin-right:0px">　　6. 更多的技术用语和符号。辨认装饰音，包括用正确的装饰音符号代替在乐谱中实际写出来的相关音符，至于有一段为人声或乐器创作的乐曲的题目则会包括各种声部和乐器名称，所使用的谱号，不同的乐器种类和它们的基本发声原理，和一些在乐谱中观察得到的特点，以测验考生把理论知识应用在实际音乐的能力。</div>

<div style="margin-left:0px; margin-right:0px">&nbsp;</div>

<div style="margin-left:0px; margin-right:0px"><strong>［主动学习与被动学习的差别］</strong></div>

<div style="margin-left:0px; margin-right:0px">　　英国皇家音乐学院的音乐定级考试由易到难分为 1 &mdash; 8 级。刚刚起步的初学者可参加简单的预备测试作为级别考试的热身；音乐考试内容涵盖广泛，其中包括了曲目演奏、视唱练耳、视奏 ( 唱 ) 乐理笔试等多个方面。联合委员会音乐考级注重对考生把理论运用于实际能力的考察，而且更注重考生对音乐的理解力及表现力。</div>

<div style="margin-left:0px; margin-right:0px">　　如果考生想继续向专业级别迈进，委员会还为较高水平及专业人士开设专业文凭的考试。八级后可参加 DIPABRSM( 文凭 ) 、 LRSM( 高级文凭 ) 、 FRSM( 院士文凭 ) 三个专业文凭考试。持有这些文凭即相当于英国皇家音乐学院颁发的文凭 LRAM 及 ARCM。</div>

<div style="margin-left:0px; margin-right:0px">　　纵观这一切，相信专业资深的钢琴老师已能对国外 ( 英皇 ) 的考级有一定的了解，国内考级与国外的考级哪种更具科学性，更能带动古典音乐的普及，相信每位老师心中都有答案。国内的音乐教育全靠教师手把手地口传心授，教师凭经验教，学生被动地学，而国外的音乐教育强调学生主动地学，要求学生大量地浏览音乐文献，了解作家及作品的背景、风格体现等等，甚至要听大量的音响资料，来让自己的演奏更具说服力和感染力，有个人的见解而不是老师教我该怎么怎么处理。</div>

<div style="margin-left:0px; margin-right:0px">　　我是一名教师，我传授的钢琴艺术本是西方文化。要想全面地提高人们欣赏古典音乐的水平，有许多地方我们还需要先进的教学 ( 考级 ) 系统与科学教学手段相结合，让我们的学生既能具有过硬的技巧，也能得到音乐修养的全面提高。</div>
</div>
'''

content = re.sub("<.*?>", "", content)
ret = client.keyword(title, content)
print(ret)
