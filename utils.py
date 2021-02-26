import html
from IPython.core.display import display, HTML

def html_escape(text):
    return html.escape(text)

def show(tokens, tags, idx, colors=None):
    
    sent = []
    BIOs = []
    for tk, lb in zip(tokens[idx].split(), tags[idx].split()):
        if tk in ['[CLS]', '[SEP]', '[PAD]']:
            continue
        sent.append(tk)
        if lb == -100: #word piece follows the previous
            BIOs.append(BIOs[-1])
        else:
            BIOs.append(lb)
    
    text_plot = sent
    wt = []
    for item in BIOs:
        if 'B' in item:
            wt.append(1)
        elif 'I' in item:
            wt.append(0.5)
        else:
            wt.append(0)
    
    if colors:
        cs = []
        for item in BIOs:
            for key in colors:
                if key in item:
                    cs.append(colors[key])
                    continue
        
    
    highlighted_text = []
    if not colors:
        for word, wt in zip(text_plot, wt):
            weight = wt

            if weight is not None:
                span = '<span style="background-color:rgba(135,206,250,'
                span += str(weight)
                span += ');">'
                span += html_escape(word)
                span += '</span>'
                
                highlighted_text.append(span)
            else:
                highlighted_text.append(word)
    else:
        for word, wt, c in zip(text_plot, wt, cs):
            weight = wt

            if weight is not None:
                span = '<span style="background-color:rgba('
                span += str(c)
                span += ','
                span += str(weight)
                span += ');">'
                span += html_escape(word)
                span += '</span>'
                
                highlighted_text.append(span)
                
#                 highlighted_text.append(f'<span style="background-color:rgba({c},' + str(weight) + ');">' + html_escape(word) + '</span>')
            else:
                highlighted_text.append(word)
    highlighted_text = ' '.join(highlighted_text)
    display(HTML(highlighted_text))
    
colors = {
    'common-ground': '139,255,252',
    'anecdote': '123,255,108',
    'statistics': '255,108,255',
    'assumption': '104,104,255',
    'other': '255,255,104',
    'testimony': '255,114,104',
    'O': '255,255,255'
}