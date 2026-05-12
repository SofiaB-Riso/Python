#Aula 2
#Criação de currículo utilizando flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Janaína Duarte</title>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Inter', sans-serif;
                    background: #f0f4f8;
                    color: #2d3748;
                    min-height: 100vh;
                    padding: 40px 20px;
                }

                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: #ffffff;
                    border-radius: 16px;
                    overflow: hidden;
                    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.12);
                }

                /* ── Cabeçalho ── */
                .header {
                    background: linear-gradient(135deg, #1a202c 0%, #2d3748 60%, #4a5568 100%);
                    color: #ffffff;
                    padding: 50px 48px 40px;
                    position: relative;
                    overflow: hidden;
                }

                .header::before {
                    content: '';
                    position: absolute;
                    top: -60px;
                    right: -60px;
                    width: 220px;
                    height: 220px;
                    background: rgba(255, 255, 255, 0.05);
                    border-radius: 50%;
                }

                .header::after {
                    content: '';
                    position: absolute;
                    bottom: -40px;
                    right: 80px;
                    width: 140px;
                    height: 140px;
                    background: rgba(255, 255, 255, 0.04);
                    border-radius: 50%;
                }

                .avatar {
                    width: 80px;
                    height: 80px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 32px;
                    font-weight: 700;
                    color: #fff;
                    margin-bottom: 20px;
                    border: 3px solid rgba(255,255,255,0.2);
                }

                .header h1 {
                    font-size: 2rem;
                    font-weight: 700;
                    letter-spacing: -0.5px;
                    margin-bottom: 6px;
                }

                .header .subtitle {
                    font-size: 1rem;
                    font-weight: 400;
                    color: rgba(255, 255, 255, 0.7);
                    margin-bottom: 24px;
                }

                .contact-bar {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    margin-top: 4px;
                }

                .contact-item {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    font-size: 0.875rem;
                    color: rgba(255, 255, 255, 0.85);
                }

                .contact-item .icon {
                    width: 32px;
                    height: 32px;
                    background: rgba(255, 255, 255, 0.12);
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 14px;
                }

                /* ── Conteúdo principal ── */
                .content {
                    padding: 40px 48px;
                }

                .section {
                    margin-bottom: 40px;
                }

                .section-title {
                    font-size: 0.7rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    color: #718096;
                    margin-bottom: 20px;
                    display: flex;
                    align-items: center;
                    gap: 12px;
                }

                .section-title::after {
                    content: '';
                    flex: 1;
                    height: 1px;
                    background: #e2e8f0;
                }

                /* ── Card de experiência ── */
                .experience-card {
                    background: #f7fafc;
                    border: 1px solid #e2e8f0;
                    border-left: 4px solid #667eea;
                    border-radius: 12px;
                    padding: 24px 28px;
                    position: relative;
                    transition: box-shadow 0.2s;
                }

                .experience-card:hover {
                    box-shadow: 0 4px 16px rgba(102, 126, 234, 0.12);
                }

                .exp-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-bottom: 8px;
                }

                .exp-role {
                    font-size: 1.1rem;
                    font-weight: 600;
                    color: #1a202c;
                }

                .exp-period {
                    background: #edf2ff;
                    color: #5a67d8;
                    font-size: 0.78rem;
                    font-weight: 600;
                    padding: 4px 12px;
                    border-radius: 20px;
                    white-space: nowrap;
                }

                .exp-company {
                    font-size: 0.9rem;
                    color: #718096;
                    font-weight: 500;
                }

                /* ── Informações pessoais ── */
                .info-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 16px;
                }

                .info-card {
                    background: #f7fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 18px 20px;
                    display: flex;
                    align-items: center;
                    gap: 14px;
                }

                .info-icon {
                    width: 42px;
                    height: 42px;
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 18px;
                    flex-shrink: 0;
                }

                .info-icon.purple { background: #f3e8ff; }
                .info-icon.blue   { background: #ebf8ff; }
                .info-icon.green  { background: #f0fff4; }

                .info-label {
                    font-size: 0.72rem;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.8px;
                    color: #a0aec0;
                    margin-bottom: 3px;
                }

                .info-value {
                    font-size: 0.9rem;
                    font-weight: 500;
                    color: #2d3748;
                    word-break: break-word;
                }

                /* ── Rodapé ── */
                .footer {
                    text-align: center;
                    padding: 20px;
                    font-size: 0.78rem;
                    color: #a0aec0;
                    border-top: 1px solid #e2e8f0;
                }

                @media (max-width: 600px) {
                    .header, .content { padding: 32px 24px; }
                    .header h1 { font-size: 1.6rem; }
                    .contact-bar { flex-direction: column; gap: 12px; }
                }
            </style>
        </head>
        <body>
            <div class="container">

                <!-- Cabeçalho -->
                <div class="header">
                    <div class="avatar">SBR</div>
                    <h1>Sofia Braga Riso</h1>
                    <p class="subtitle">Desenvolvedora</p>
                    <div class="contact-bar">
                        <div class="contact-item">
                            <div class="icon">✉</div>
                            sbriso2020@gmail.com.
                        </div>
                        <div class="contact-item">
                            <div class="icon">📱</div>
                            (31) 99999-9999
                        </div>
                    </div>
                </div>

                <!-- Conteúdo -->
                <div class="content">

                    <!-- Informações Pessoais -->
                    <div class="section">
                        <div class="section-title">Informações Pessoais</div>
                        <div class="info-grid">
                            <div class="info-card">
                                <div class="info-icon purple">👤</div>
                                <div>
                                    <div class="info-label">Nome</div>
                                    <div class="info-value">Sofia Braga</div>
                                </div>
                            </div>
                            <div class="info-card">
                                <div class="info-icon blue">✉</div>
                                <div>
                                    <div class="info-label">E-mail</div>
                                    <div class="info-value">sbriso2020@gmail.com</div>
                                </div>
                            </div>
                            <div class="info-card">
                                <div class="info-icon green">📱</div>
                                <div>
                                    <div class="info-label">Telefone</div>
                                    <div class="info-value">(31) 99999-9999</div>
                                </div>
                            </div>
                        </div>
                    </div>

                <div class="footer">
                    Currículo gerado com Flask &mdash; Sofia Braga &copy; 2025
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)