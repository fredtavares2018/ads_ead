
--
-- Banco de Dados: `port_fazentech`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios_fazentech`
--

CREATE TABLE IF NOT EXISTS `funcionarios_fazentech` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpf` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `rg` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nome` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `apelido` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cep` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `endereco` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero` int(11) NOT NULL,
  `bairro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `complemento` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `uf` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `celular` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `experiencia` text COLLATE utf8_unicode_ci NOT NULL,
  `cargo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `salario` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `obs` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`,`cpf`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;


--
-- Estrutura da tabela `varejistas_fazentech`
--

CREATE TABLE IF NOT EXISTS `varejistas_fazentech` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cnpj` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nome_empresa` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cep` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `endereco` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero` int(11) NOT NULL,
  `bairro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `complemento` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `uf` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `telefone` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `celular` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_prodduto` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `obs` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`,`cnpj`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;


--
-- Estrutura da tabela `equipamentos_fazentech`
--

CREATE TABLE IF NOT EXISTS `equipamentos_fazentech` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `numero_serie` int(5) NOT NULL,
  `tipo_proprio_alugado` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `valor_aluguel_hora` date COLLATE utf8_unicode_ci NOT NULL,
  `tempo_aluguel` date COLLATE utf8_unicode_ci NOT NULL,
  `prorrogado` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `data_pagamento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `forma_pagamento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `parcela` int(20) NOT NULL,
  `acrescimo` int(20) NOT NULL,
  `desconto` int(20) NOT NULL,
  `total` int(20) NOT NULL,
  `obs` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`,`numero_serie`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;


--
-- Estrutura da tabela `pagamentos_clientes`
--

CREATE TABLE IF NOT EXISTS `pagamentos_clientes` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_varejista` int(10) NOT NULL,
  `numero_doc` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `serie` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `emissao` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `vencimento` date COLLATE utf8_unicode_ci NOT NULL,
  `prorrogado` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `centro_de_custo` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `pagamento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `forma_pagamento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `baixar` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `parcela` int(20) NOT NULL,
  `valor` int(20) NOT NULL,
  `acrescimo` int(20) NOT NULL,
  `desconto` int(20) NOT NULL,
  `total` int(20) NOT NULL,
  `obs` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;

--
-- Estrutura da tabela `producao_leite`
--

CREATE TABLE IF NOT EXISTS `producao_leite` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `identificacao` int(10) NOT NULL,
  `especie` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `data_ultima_ordenha` date NOT NULL,
  `temperatura_do_leite` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `produtividade_parto` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `inseminacao_data` date NOT NULL,
  `estimativa_do_parto` date NOT NULL,
  `parto_custo` int(12) NOT NULL,
  `secagem_esperada` varchar(120) COLLATE utf8_unicode_ciNOT NULL,
  `minutos_de_ruminacao_dia` int(20) NOT NULL,
  `ruminacao_dia_kg` int(20) NOT NULL,
  `obs` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`,`identificacao`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;


--
-- Estrutura da tabela `produtos_produzidos`
--

CREATE TABLE IF NOT EXISTS `produtos_produzidos` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `quantidade` int(10) NOT NULL,
  `produto` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_produto` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  `desconto` int(20) NOT NULL,
  `preco_unitario` int(20) NOT NULL,
  `preco_kg` int(20) NOT NULL,
  `total_estoque` int(20) NOT NULL,
  `obs` varchar(2000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;
